import os
import smtplib
import unittest
#HTMLTestRunner是基于unittest框架的一个扩展,可以自己在网上下载
import time
from email.header import Header
from email.mime.text import MIMEText

from lib.HTMLTestRunner import HTMLTestRunner


def send_mail(path):
    f = open(path,'rb')
    mail_body = f.read()
    f.close()#读取文件内容
    #要想发邮件,要把二进制的内容转成MIME格式
    #MIME multipurse 多用途 Internet 互联网 Mail 邮件 Extension 扩展
    #MIME是对邮件协议的一个扩展,使邮件不仅支持文本格式还支持多种格式,比如说图片,音频,二进制文件
    msg = MIMEText(mail_body,'html','utf-8')
    msg['Subject'] = Header("自动化测试报告","utf-8")#设置邮件主题
    #需要设置客户端授权码,为了安全性,设置->邮箱安全设置->客户端授权
    msg['From'] = 'tianzhenzhen0429@163.com'
    msg['To'] = 'wuyun2008@126.com;qiwenyanzi@163.com'
    #发邮件的步骤
    #1.打开登陆页面,连接邮箱服务器(需知道网络传输协议http,https,ftp,socket)
    #发邮件的协议:pop3,smtp,imap
    #smtp simple mail transful protocol 简单邮件传输协议
    smtp = smtplib.SMTP()
    smtp.connect("smtp.163.com")
    #2.登录邮箱
    smtp.login('tianzhenzhen0429@163.com','1234qwer')
    #3.发送邮件
    smtp.sendmail(msg['From'],msg['To'], msg.as_string())
    #smtp.sendmail('bwftest126@126.com','1049368167@qq.com', msg.as_string())
    #4.退出邮箱
    smtp.quit()
    print("email has sent out!")


if __name__ == '__main__':
    #通过这个方法strftime()可以定义当前时间的格式
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    suite = unittest.defaultTestLoader.discover('./day5','*Test.py')
    unittest.TextTestRunner() #文本测试用例运行器
    #现在用html的测试用例运行器
    #html会生成html格式的测试报告,需要指定路径
    base_path = os.path.dirname(__file__)
    path = base_path + "/report/report" + now + ".html"
    file = open(path,'wb')
    HTMLTestRunner(stream=file,title="海盗商城测试报告", description="测试环境:window server 2008 + Chrome").run(suite)
    file.close()
    #把html格式的报告作为文件正文,发送邮件
    send_mail(path)
    #这时生成的测试报告只显示类名和方法名,只能给专业的人看,我们应该把相关的手动测试用例的标题加到报告里
    #加一个时间戳,区分报告
    #当测试报告生成后,生成邮件,通知关心测试结果的人
