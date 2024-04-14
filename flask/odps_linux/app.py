
from flask import Flask, render_template
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType

import odps_text
from odps_text import odsp_t
import send_e

from pyecharts import options as opts
from pyecharts.charts import Line, Bar, Polar

app = Flask(__name__, static_folder="templates")

data = odps_text.odsp_t()
pre_data_k = list(send_e.check_dict(data).keys())
send_e.send_e(send_e.check_pre(send_e.check_dict(data)), pre_data_k)
# CORS(app, supports_credentials=True)


@app.after_request
def cors(environ):
    environ.headers['Access-Control-Allow-Origin'] = '*'
    environ.headers['Access-Control-Allow-Method'] = '*'
    environ.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return environ


def line_base() -> Line:
    l = (
        Line()
            .add_xaxis(list(odsp_t().locate))
            # .add_yaxis("频率", list(odsp_t().su))
            .add_yaxis("频率", [5, 5, 5, 5, 5, 5, 5, 4, 5, 5])
            .set_global_opts(title_opts=opts.TitleOpts(title="", subtitle=""))

    )
    return l


def bar_base() -> Bar:
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add_xaxis(list(odsp_t().locate))
            # .add_yaxis("频率", list(odsp_t().su))
            .add_yaxis("频率", [5, 5, 5, 5, 5, 5, 5, 4, 5, 5])
            .set_global_opts(title_opts=opts.TitleOpts(title="", subtitle=""))
    )
    return c


def polar_base() -> Polar:
    p = (
        Polar()
            .add_schema(
            radiusaxis_opts=opts.RadiusAxisOpts(data=Faker.week, type_="category")
        )
            .add(pre_data_k[0], [1, 1, 1, 1, 1, 1, 1], type_="bar", stack="stack0")
            .add(pre_data_k[1], [1, 1, 1, 1, 1, 1, 1], type_="bar", stack="stack0")
            .add(pre_data_k[2], [1, 1, 1, 1, 1, 1, 1], type_="bar", stack="stack0")
            .add(pre_data_k[3], [1, 1, 1, 1, 1, 1, 1], type_="bar", stack="stack0")
            .add(pre_data_k[4], [1, 1, 1, 1, 1, 1, 1], type_="bar", stack="stack0")
            .add(pre_data_k[5], [1, 1, 1, 1, 1, 1, 1], type_="bar", stack="stack0")
            .add(pre_data_k[6], [1, 1, 1, 1, 1, 1, 1], type_="bar", stack="stack0")
            .add(pre_data_k[7], [1, 1, 1, 1, 1, 0, 1], type_="bar", stack="stack0")

            .set_global_opts(title_opts=opts.TitleOpts(title=""))
    )
    return p

@app.route("/")
def index():
    return render_template("/index.html")


@app.route("/lineChart")
def get_line_chart():
    l = line_base()
    return l.dump_options_with_quotes()


@app.route("/barChart")
def get_bar_chart():
    c = bar_base()
    return c.dump_options_with_quotes()

@app.route("/polarChart")
def get_polar_chart():
    p = polar_base()
    return p.dump_options_with_quotes()


if __name__ == "__main__":
    app.run()
