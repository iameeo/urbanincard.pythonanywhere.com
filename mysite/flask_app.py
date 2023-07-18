from flask import Flask, request, redirect
from flask import render_template
from flask_mail import Mail, Message
from datetime import date
from flask_mobility import Mobility
import requests

app = Flask(__name__)

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = "urban.incard@gmail.com"
app.config["MAIL_PASSWORD"] = "gyhfvunuwlxdqewa"
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True

email = Mail(app)
Mobility(app)

@app.route('/', methods = ["get"])
def Index():
    path = 'Index'
    today = date.today().year
    model = {
        "path" : path
        ,"today" : today
    }
    return render_template('Index.html', model=model)

@app.route('/Wedding', methods = ["get"])
def Wedding():
    path = 'Wedding'
    today = date.today().year
    return render_template('Wedding.html', path=path, today=today)

@app.route('/Baby', methods = ["get"])
def Baby():
    path = 'Baby'
    today = date.today().year
    return render_template('Baby.html', path=path, today=today)

@app.route('/Event', methods = ["get"])
def Event():
    path = 'Event'
    today = date.today().year
    return render_template('Event.html', path=path, today=today)

@app.route('/Thanks', methods = ["get"])
def Thanks():
    path = 'Thanks'
    today = date.today().year
    return render_template('Thanks.html', path=path, today=today)

@app.route('/Sample/<urlPath>', methods = ["get"])
def sample(urlPath):
    path = 'Sample'
    type = urlPath
    return render_template('/Sample/'+ urlPath + '.html', path=path,type=type)

@app.route('/Order/', methods = ["get"])
def Order():
    path = 'Order'
    today = date.today().year
    return render_template('/Order/Order.html', path=path, today=today)

@app.route('/Order/Post', methods = ["post"])
def OrderPost():
    emailBody = ""
    emailBody = emailBody = "<style>	body{background-color:#fff;}	input {width:305px;padding:10px 5px;margin:5px 0px;border:1px solid #eaeaea;-webkit-appearance: none;   -webkit-border-radius: 0;}	td{text-align:left;border:1px solid #eaeaea;}	.label{font-size:12px;color:#000;font-weight:normal;}</style>"
    emailBody = emailBody + \
        "<div style='width:320px;margin:0 auto;text-align:center;padding:10px;'>"
    emailBody = emailBody + "    <input type='hidden' name='t_shop' value=''>"
    emailBody = emailBody + "    <input type='hidden' name='t_seq' value=''>"
    emailBody = emailBody + \
        "    <table border='0' width='100%' cellpadding='0' cellspacing='0'>"
    emailBody = emailBody + "    <tbody><tr>"
    emailBody = emailBody + "        <td><img src='https://shop-phinf.pstatic.net/20190824_74/ncp_1noygk_01_1566610931376ayLsD_JPEG/54665007578302011_462928582.jpg?type=w345' style='width:150px;'></td>"
    emailBody = emailBody + "    </tr>"
    emailBody = emailBody + "    <tr>"
    emailBody = emailBody + \
        "        <td><span style='font-weight:bold;background-color:#eaeaea;'>어반인카드 주문서</span></td>"
    emailBody = emailBody + "    </tr>"
    emailBody = emailBody + "    <tr>"
    emailBody = emailBody + "        <td class='label'>스토어</td>"
    emailBody = emailBody + "    </tr>"
    emailBody = emailBody + "    <tr>"
    emailBody = emailBody + "        <td>" + \
        request.form['t_shop'] + "</td>"
    emailBody = emailBody + "    </tr>"
    emailBody = emailBody + "    <tr> <td>&nbsp;</td> </tr>"
    emailBody = emailBody + "    <tr>"
    emailBody = emailBody + "        <td class='label'>상품번호</td>"
    emailBody = emailBody + "    </tr>"
    emailBody = emailBody + "    <tr>"
    emailBody = emailBody + "        <td>" + \
        request.form['t_seq'] + "</td>"
    emailBody = emailBody + "    </tr>"
    emailBody = emailBody + "    <tr> <td>&nbsp;</td> </tr>"
    emailBody = emailBody + "    <tr>"
    emailBody = emailBody + "        <td class='label'>주문자명</td>"
    emailBody = emailBody + "    </tr>"
    emailBody = emailBody + "    <tr>"
    emailBody = emailBody + "        <td>" + \
        request.form['order_name'] + "</td>"
    emailBody = emailBody + "    </tr>"
    emailBody = emailBody + "    <tr> <td>&nbsp;</td> </tr>"
    emailBody = emailBody + "    <tr>"
    emailBody = emailBody + "        <td class='label'>신랑명</td>"
    emailBody = emailBody + "    </tr>"
    emailBody = emailBody + "    <tr>"
    emailBody = emailBody + "        <td>" + \
        request.form['man_name'] + "</td>"
    emailBody = emailBody + "    </tr>"
    emailBody = emailBody + "    <tr> <td>&nbsp;</td> </tr>"
    emailBody = emailBody + "    <tr>"
    emailBody = emailBody + "        <td class='label'>신부명</td>"
    emailBody = emailBody + "    </tr>"
    emailBody = emailBody + "    <tr>"
    emailBody = emailBody + "        <td>" + \
        request.form['woman_name'] + "</td>"
    emailBody = emailBody + "    </tr>"
    emailBody = emailBody + "    <tr> <td>&nbsp;</td> </tr>"
    emailBody = emailBody + "    <tr>"
    emailBody = emailBody + "        <td class='label'>신랑혼주</td>"
    emailBody = emailBody + "    </tr>"
    emailBody = emailBody + "    <tr>"
    emailBody = emailBody + "        <td>" + \
        request.form['man_parent'] + "</td>"
    emailBody = emailBody + "    </tr>"
    emailBody = emailBody + "    <tr> <td>&nbsp;</td> </tr>"
    emailBody = emailBody + "    <tr>"
    emailBody = emailBody + "        <td class='label'>신부혼주</td>"
    emailBody = emailBody + "    </tr>"
    emailBody = emailBody + "    <tr>"
    emailBody = emailBody + "        <td>" + \
        request.form['woman_parent'] + "</td>"
    emailBody = emailBody + "    </tr>"
    emailBody = emailBody + "    <tr> <td>&nbsp;</td> </tr>"
    emailBody = emailBody + "    <tr>"
    emailBody = emailBody + "        <td class='label'>결혼식장</td>"
    emailBody = emailBody + "    </tr>"
    emailBody = emailBody + "    <tr>"
    emailBody = emailBody + "        <td>" + \
        request.form['address'] + "</td>"
    emailBody = emailBody + "    </tr>"
    emailBody = emailBody + "    <tr> <td>&nbsp;</td> </tr>"
    emailBody = emailBody + "    <tr>"
    emailBody = emailBody + "        <td class='label'>결혼식날짜</td>"
    emailBody = emailBody + "    </tr>"
    emailBody = emailBody + "    <tr>"
    emailBody = emailBody + "        <td>" + \
        request.form['weddingdate'] + "</td>"
    emailBody = emailBody + "    </tr>"
    emailBody = emailBody + "    <tr> <td>&nbsp;</td> </tr>"
    emailBody = emailBody + "    <tr>"
    emailBody = emailBody + "        <td class='label'>결혼식시간</td>"
    emailBody = emailBody + "    </tr>"
    emailBody = emailBody + "    <tr>"
    emailBody = emailBody + "        <td>" + \
        request.form['weddingtime'] + "</td>"
    emailBody = emailBody + "    </tr>"
    emailBody = emailBody + "    <tr> <td>&nbsp;</td> </tr>"
    emailBody = emailBody + "    <tr>"
    emailBody = emailBody + "        <td class='label'>첨부파일</td>"
    emailBody = emailBody + "    </tr>"
    emailBody = emailBody + "    <tr>"
    emailBody = emailBody + "        <td>1</td>"
    emailBody = emailBody + "    </tr>"
    emailBody = emailBody + "    <tr> <td>&nbsp;</td> </tr>"
    emailBody = emailBody + "    <tr>"
    emailBody = emailBody + "        <td class='label'>문의내용</td>"
    emailBody = emailBody + "    </tr>"
    emailBody = emailBody + "    <tr>"
    emailBody = emailBody + "        <td>"
    emailBody = emailBody + "            " + request.form['etc']
    emailBody = emailBody + "        </td>"
    emailBody = emailBody + "    </tr>"
    emailBody = emailBody + "    </tbody></table>"
    emailBody = emailBody + "</div>"

    title = request.form['order_name'] + " - 어반인카드 주문서"
    content = emailBody
    msg = Message(
        f"{title}",
        body=f"{content}",
        sender="urban.incard@gmail.com",
        recipients=["joowon1028@gmail.com"],
    )
    email.send(msg)

    return redirect('/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
