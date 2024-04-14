import odps_text
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = '2497122877@qq.com'  # 发件人邮箱账号
my_pass = 'dzvzdglkyqlldjbj'  # 发件人邮箱密码
my_user = '2497122877@qq.com'  # 收件人邮箱账号，我这边发送给自己

data = odps_text.odsp_t()


def check_dict(data):
    key = list(data.locate)
    # value = list(data.su)
    value = [5, 5, 5, 5, 5, 5, 5, 4, 5, 5]
    dic = dict(zip(key, value))
    # dic_re=
    return dic


def check_pre(dic):
    # date = 10  # 测试数据，每个启动5次，先写死，下来可调整为巡检端启动次数
    date = 5
    pre_data_v = list(check_dict(data).values())
    pre_data_k = list(check_dict(data).keys())
    # print(pre_data_v)
    err = []
    for check in range(0, len(pre_data_v)):
        if pre_data_v[check] != date:
            err.append(check)
            print(err)
        else:
            continue
    return err


def send_e(err, pre_data_k):
    if err == []:
        return 0
    else:
        save_k = []
        for i in err:
            save_k.append(pre_data_k[i])
            # print(type(i))
        ret = True
        try:
            msg = MIMEText("您于今日所巡检结果中{}出现异常，请进行确认，避免不必要损失".format(save_k), 'plain', 'utf-8')
            msg['From'] = formataddr(["spark", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To'] = formataddr(["wx", '2558740197@qq.com'])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = "预警信息"  # 邮件的主题，也可以说是标题

            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
            server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(my_sender, ['2558740197@qq.com', ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            ret = False
        return ret


pre_data_k = list(check_dict(data).keys())
send_e(check_pre(check_dict(data)), pre_data_k)
