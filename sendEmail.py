#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

# 第三方 SMTP 服务
mail_host="smtp.126.com"  #设置服务器
mail_user="guantbb@126.com"    #用户名
mail_pass="ZYHFDEQDVPBOODXJ"   #口令 

sender = 'guantbb@126.com'
receivers = ['guantbb@126.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('测试邮件内容_____当你收到这份邮件，说明我使用python发送邮件成功了', 'plain', 'utf-8')
message['From'] = formataddr(["AndrewPython", sender])  # 括号里对应的分别是邮箱昵称、发件人邮箱账号
message['To'] = formataddr(["AndrewGongUnisoc", sender])  # 括号里的对应收件人邮箱昵称、收件人邮箱账
message['Subject'] = "Python发送邮件测试。"  # 邮件的主题，也可以说是标题

try:
    server = smtplib.SMTP(mail_host) 
    server.login(mail_user,mail_pass)
    server.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")