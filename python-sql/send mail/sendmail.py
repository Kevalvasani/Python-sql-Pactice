import os
import ssl
import smtplib
from email.message import EmailMessage

email_sender="kevalvasani1910@gmail.com"
email_password=os.environ.get("EMAIL_PASSWORD")
email_reciever="kevalpython@gmail.com"

subject="my first mail practice"
body="""
My name is keval vasani and i am python developer.
This is my first mail send by python.
"""

em= EmailMessage()
em['From']=email_sender
em['To']=email_reciever
em['Subject']=subject
em.set_content(body)

context=ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_reciever,em.as_string())