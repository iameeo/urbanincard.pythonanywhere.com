from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
#import datetime


def index(request):
    if request.method == 'POST':
        #now = datetime.datetime.now()
        #nowTime = now.strftime('%H:%M:%S')
        #uploadFileName = request.POST['weddingdate'] + request.POST['weddingtime'] + nowTime
        # print(uploadFileName)

        myfile = request.FILES['file1']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)

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
            request.POST['t_shop'] + "</td>"
        emailBody = emailBody + "    </tr>"
        emailBody = emailBody + "    <tr> <td>&nbsp;</td> </tr>"
        emailBody = emailBody + "    <tr>"
        emailBody = emailBody + "        <td class='label'>상품번호</td>"
        emailBody = emailBody + "    </tr>"
        emailBody = emailBody + "    <tr>"
        emailBody = emailBody + "        <td>" + \
            request.POST['t_seq'] + "</td>"
        emailBody = emailBody + "    </tr>"
        emailBody = emailBody + "    <tr> <td>&nbsp;</td> </tr>"
        emailBody = emailBody + "    <tr>"
        emailBody = emailBody + "        <td class='label'>주문자명</td>"
        emailBody = emailBody + "    </tr>"
        emailBody = emailBody + "    <tr>"
        emailBody = emailBody + "        <td>" + \
            request.POST['order_name'] + "</td>"
        emailBody = emailBody + "    </tr>"
        emailBody = emailBody + "    <tr> <td>&nbsp;</td> </tr>"
        emailBody = emailBody + "    <tr>"
        emailBody = emailBody + "        <td class='label'>신랑명</td>"
        emailBody = emailBody + "    </tr>"
        emailBody = emailBody + "    <tr>"
        emailBody = emailBody + "        <td>" + \
            request.POST['man_name'] + "</td>"
        emailBody = emailBody + "    </tr>"
        emailBody = emailBody + "    <tr> <td>&nbsp;</td> </tr>"
        emailBody = emailBody + "    <tr>"
        emailBody = emailBody + "        <td class='label'>신부명</td>"
        emailBody = emailBody + "    </tr>"
        emailBody = emailBody + "    <tr>"
        emailBody = emailBody + "        <td>" + \
            request.POST['woman_name'] + "</td>"
        emailBody = emailBody + "    </tr>"
        emailBody = emailBody + "    <tr> <td>&nbsp;</td> </tr>"
        emailBody = emailBody + "    <tr>"
        emailBody = emailBody + "        <td class='label'>신랑혼주</td>"
        emailBody = emailBody + "    </tr>"
        emailBody = emailBody + "    <tr>"
        emailBody = emailBody + "        <td>" + \
            request.POST['man_parent'] + "</td>"
        emailBody = emailBody + "    </tr>"
        emailBody = emailBody + "    <tr> <td>&nbsp;</td> </tr>"
        emailBody = emailBody + "    <tr>"
        emailBody = emailBody + "        <td class='label'>신부혼주</td>"
        emailBody = emailBody + "    </tr>"
        emailBody = emailBody + "    <tr>"
        emailBody = emailBody + "        <td>" + \
            request.POST['woman_parent'] + "</td>"
        emailBody = emailBody + "    </tr>"
        emailBody = emailBody + "    <tr> <td>&nbsp;</td> </tr>"
        emailBody = emailBody + "    <tr>"
        emailBody = emailBody + "        <td class='label'>결혼식장</td>"
        emailBody = emailBody + "    </tr>"
        emailBody = emailBody + "    <tr>"
        emailBody = emailBody + "        <td>" + \
            request.POST['address'] + "</td>"
        emailBody = emailBody + "    </tr>"
        emailBody = emailBody + "    <tr> <td>&nbsp;</td> </tr>"
        emailBody = emailBody + "    <tr>"
        emailBody = emailBody + "        <td class='label'>결혼식날짜</td>"
        emailBody = emailBody + "    </tr>"
        emailBody = emailBody + "    <tr>"
        emailBody = emailBody + "        <td>" + \
            request.POST['weddingdate'] + "</td>"
        emailBody = emailBody + "    </tr>"
        emailBody = emailBody + "    <tr> <td>&nbsp;</td> </tr>"
        emailBody = emailBody + "    <tr>"
        emailBody = emailBody + "        <td class='label'>결혼식시간</td>"
        emailBody = emailBody + "    </tr>"
        emailBody = emailBody + "    <tr>"
        emailBody = emailBody + "        <td>" + \
            request.POST['weddingtime'] + "</td>"
        emailBody = emailBody + "    </tr>"
        emailBody = emailBody + "    <tr> <td>&nbsp;</td> </tr>"
        emailBody = emailBody + "    <tr>"
        emailBody = emailBody + "        <td class='label'>첨부파일</td>"
        emailBody = emailBody + "    </tr>"
        emailBody = emailBody + "    <tr>"
        emailBody = emailBody + "        <td>" + filename + "</td>"
        emailBody = emailBody + "    </tr>"
        emailBody = emailBody + "    <tr> <td>&nbsp;</td> </tr>"
        emailBody = emailBody + "    <tr>"
        emailBody = emailBody + "        <td class='label'>문의내용</td>"
        emailBody = emailBody + "    </tr>"
        emailBody = emailBody + "    <tr>"
        emailBody = emailBody + "        <td>"
        emailBody = emailBody + "            " + request.POST['etc']
        emailBody = emailBody + "        </td>"
        emailBody = emailBody + "    </tr>"
        emailBody = emailBody + "    </tbody></table>"
        emailBody = emailBody + "</div>"

        email = EmailMessage(
            request.POST['order_name'] + " - 어반인카드 주문서", emailBody, to=['joowon1028@gmail.com'])
        email.attach_file(settings.MEDIA_ROOT + '/'+filename)
        email.content_subtype = "html"
        email.send()

        os.remove(settings.MEDIA_ROOT + '/'+filename)

        return redirect('/')

    elif request.method == 'GET':
        context = {}
        return render(request, 'index.html', context)
