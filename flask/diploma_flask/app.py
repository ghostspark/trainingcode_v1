from flask import Flask, render_template, redirect, session, request, g
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

import sql
import sql_settings
from sql_exts import db
from static.blue_log.form import loginForm
from static.blue_register import register_blue
from static.blue_properties import properties_blue
from static.blue_log import log_blue
from static.blue_root import root_blue
from static.blue_user import user_blue

app = Flask(__name__, static_folder='./static')
app.secret_key = 'dlr key'
bootstrap = Bootstrap(app)

app.config.from_object(sql_settings)
db.init_app(app)


@app.before_request  # 拦截器
def before():
    _id = session.get("name", None)
    url = request.path
    PassUrl = ['/', '/index', '/register']
    if url in PassUrl:
        pass
    else:
        _id = session.get("name", None)
        if not _id:
            return redirect("/")
        else:
            pass


@app.route('/', methods=['GET', 'POST'])  # login
def login():
    form = loginForm()
    if request.method == 'POST':
        session['name'] = form.name.data
        session['password'] = form.Password.data
        print(session.values())
        data = [{'name': form.name.data, 'pw': form.Password.data, 'remember': form.Remember.data}]
        if data[0]['name'] == sql.mysql_select_user(data[0]['name'])[0] and data[0]['pw'] == \
                sql.mysql_select_user(name=data[0]['name'])[1]:
            if sql.mysql_select_user(data[0]['name'])[3] == '0':
                return redirect('/root')
            else:
                return redirect('/index')
        else:
            print(data)
            return render_template('./html/login.html', form=form)
    elif request.method == 'GET':
        return render_template('./html/login.html', form=form)


@app.route('/index')  # 首页
def hello_world():  # put application's code here
    return render_template("./html/index_2.html")


app.register_blueprint(properties_blue)  # 结果呈现
app.register_blueprint(register_blue)  # 注册
app.register_blueprint(root_blue)  # 管理员界面
app.register_blueprint(user_blue)  # 用户界面

if __name__ == '__main__':
    app.run()
