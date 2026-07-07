import os
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage 

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

