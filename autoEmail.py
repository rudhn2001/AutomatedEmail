import smtplib
import os
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

#setup connection  to our email server
smtp = smtplib.SMTP('smtp.gmail.com',587)
smtp.ehlo()
smtp.starttls()
smtp.login('achkerman299@gmail.com', 'twozero01')

#building the mssg content
subject="This is test mail for automated email"
msg=''' Hello\n
This is a test email and it has been successfully been recieved by another email!!!!




Thank you..... :)

Regards by yours truely \n
Anirudh S N \n'''
msg.attach(MIMEText(text))
sender = 'achkerman299@gmail.com'
reciever='anirudhsn.is19@sahyadri.edu.in'
email = EmailMessage()

email['From']=sender
email['To']=reciever
email['Subject']=subject
email.set_content()