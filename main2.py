#importing all the modules used

import csv
import  re
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage
from email.mime.text import MIMEText


#function to validate email

def Email_Validate(user_id) : 
    pattern= '([a-z 0-9_.+-]+@[a-z 0-9]+\.[a-z 0-9 .])'
    if re.search(pattern,user_id): 
        return 1
    else: 
        return 0
    
def Email_Store():
    csvFile=csv.reader(file)
    writer= csv.writer(file2)
    Email=""
    
    for email in csvFile:
        type(email)
        Email=''.join(email)
        print(Email)
        if (Email_Validate(Email)==1):
            Email_list.append(Email)
            writer.writerows(Email)
        else:
            continue
    print("A file named Valid_Mail.csv has been created to store valid emails")
    
    
    
def auto_Email():
    
    #sender 
    sender_mail=input("Enter the Sender's Email : ")
    sender_pass=input("Enter the Sender's Password : ")
    #setup connection  to our email server
    smtp = smtplib.SMTP('smtp.gmail.com',587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(sender_mail, sender_pass)
    #building the mssg content
    subject="This is test mail for automated email"
    msg=''' Hello\n
    This is a test email and it has been successfully been recieved by another email!!!!
    
    Thank you..... :)

    Regards by yours truely \n
    Anirudh S N \n'''
    
    
    #opening the CV file to read the emails
    file3=open('Valid_Mail.csv','r')

    #Reading a csv file
    csvFile=csv.reader(file3)
    for reciever in Email_list: 
        #start the message building
        email = EmailMessage()
        email['From']=sender_mail
        email['To']=reciever
        email['Subject']=subject
        email.set_content(msg)
        smtp.send_message(email)
        print(f'Email sent to {reciever}')
    smtp.close()

Email_list=[]
print("Starting the program!!!!")
file=open('Book1.csv','r')
file2=open('Valid_Mail.csv','w')
Email_Store()
print(Email_list)
print("Email's been sorted")
auto_Email()
print("Program is done")