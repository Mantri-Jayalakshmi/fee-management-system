# Send Emails to fee pending users

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

def send_mail(to_email, name):
    smtp_server = "smtp.gmail.com"
    smtp_port_number = 587
    username = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASSWORD")

    if not username or not password:
        print("DEBUG: Email credentials not found!")
        return None

    subject = "Fee Pending Status"
    body = f"Dear {name}, \nYou have a pending Fee Issue. \nPlease make sure to clear as soon as possible!"

    message = MIMEMultipart()
    message['From'] = username
    message['To'] = to_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port_number)
        server.starttls()
        server.login(username, password)
        server.send_message(message)
        server.quit()
        print(f"Mail sent to {name} successfully!")
        return True
    except Exception as e:
        print(f"Failed to send mail to {name}: {e}")
        return False