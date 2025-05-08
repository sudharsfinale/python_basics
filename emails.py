import smtplib  # Simple Mail Transfer Protocol ~ actually a protocol to send mail basically works with email services

# To send a file we use FTP ~ File Transfer Protocol as a protocol

# If we want to access world wide web we use HTTP ~ Hypertext Transfer Protocol as a protocol

# If we have to send some packets we use TCP (Transmission Control Protocol) or UDP (User Datagram Protocol)

import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

server.starttls()

server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

server.sendmail(EMAIL_ADDRESS, "sudharsfinale@gmail.com",
                "Mail send from python smtplib")

print("Mail sent")
