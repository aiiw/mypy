#!/usr/bin/python3
import smtplib
from email.mime.text import MIMEText
# 第三方 SMTP 服务
mail_host="smtp.163.com"  #设置服务器
mail_user="aliaiiw@163.com"    #用户名
mail_pass="IBPYQYJQNKZXJQMK11"   #口令 
 #IBPYQYJQNKZXJQMK
sender = 'aliaiiw@163.com'
receivers = ['alidongxing@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
message = MIMEText('content','plain','utf-8')
message['From'] = sender
message['To'] =  receivers[0]
subject = 'Python SMTP'
message['Subject'] = subject

print ("开始发送邮件")
print(message.as_string())
# smtpObj = smtplib.SMTP() 
# smtplib.SMTP_SSL(mail_host, '465')    # 25 为 SMTP 端口号
smtpObj = smtplib.SMTP() 
smtpObj.connect(mail_host,808)

smtpObj.login(mail_user,mail_pass)

smtpObj.sendmail(sender, receivers, message.as_string())

 #send_email('smtp.163.com', 'xxxx@163.com', 'xxxx', 'xxxx@163.com', '邮件标题', '邮件内容')
print ("邮件发送成功")
