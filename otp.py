# otp sending with Exception Handling

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
from dotenv import load_dotenv
import os

load_dotenv()

def send_otp(to_email):
    otp = random.randint(1111, 9999)
    print(f"DEBUG: Generated OTP:{otp}") 

    smtp_server = "smtp.gmail.com"
    smtp_port_number = 587
    username = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASSWORD")

    if not username or not password:
        print("DEBUG: Email credentials not found!")
        return None

    subject = "OTP Authentication"
    body = f"OTP for Authentication is {otp}. \nThank You" 

    message = MIMEMultipart()
    message['From'] = username
    message['To'] = to_email
    message['Subject'] = subject
    message.attach(MIMEText(body,'plain'))

    try:
        print(f"DEBUG: Connecting to SMTP server {smtp_server}:{smtp_port_number}")  # Debug        
        server = smtplib.SMTP(smtp_server,smtp_port_number)
        server.starttls()
        print("DEBUG: Logging into email...")
        server.login(username, password)
        print("DEBUG: Sending OTP email...")
        server.send_message(message)
        server.quit()
        print(f"Otp sent successfully to {to_email}")
        return otp
    except Exception as e:
        print(f"Failed to send otp: {e}")
        return None