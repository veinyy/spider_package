#!/usr/bin/env python3
#coding: utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
import time
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

list=[]
for name in range(1, 80000):
	file = str(name) + ".jpg"
	list.append(file)

file = []
for num  in range(1700, 80000):
	file.append(list[num])
	if len(file) == 80:
		sender = '442078359@qq.com'
		receiver = ['664184098@qq.com','592171154@qq.com','360272848@qq.com','654819639@qq.com','1029407694@qq.com','616846661@qq.com']
		subject = 'python email test'
		smtpserver = 'smtp.qq.com'
		username = '442078359@qq.com'
		password = '258900'
		msgRoot = MIMEMultipart('related')
		msgRoot['Subject'] = 'just see see'
		msgRoot['From']=sender 
		msgRoot['To']=';'.join(receiver) 
		msgRoot['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')
		for val in file:
			att = MIMEText(open(val, 'rb').read(), 'base64', 'utf-8')
			att["Content-Type"] = 'application/octet-stream'
			att["Content-Disposition"] = "attachment; filename=%s" % val
			msgRoot.attach(att)
		smtp = smtplib.SMTP()
		smtp.connect('smtp.qq.com')
		smtp.login(username, password)
		smtp.sendmail(sender, receiver, msgRoot.as_string())
		smtp.quit()
		time.sleep(9600)
		del file[:]
	else:
		continue
