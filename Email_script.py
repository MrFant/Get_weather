#!/usr/bin/python
# -*- coding: utf-8 -*-
import smtplib
import Get_weather
from email.mime.text import MIMEText
def Post_Email(content):
	mail_host = 'smtp.qq.com'
    # Get_weather.Get_weather()
	mail_user = '2413633136@qq.com'
	mail_pass = 'xxxxxxx'
	sender = '2413633136@qq.com'
	receivers = ['2413633136@qq.com']
	message = MIMEText(content, 'plain', 'utf-8')
	message['Subject'] = 'From fant\'s Email_Script'
	message['From'] = sender
	message['To'] = receivers[0]
	try:
		smtpObj = smtplib.SMTP()
		smtpObj = smtplib.SMTP_SSL(mail_host)
		smtpObj.login(mail_user, mail_pass)
		smtpObj.sendmail(sender, receivers, message.as_string())
		smtpObj.quit()
		#print('success')
	except smtplib.SMTPException as e:
		print('error', e)

if __name__=="__main__":
	Post_Email("model test......")



