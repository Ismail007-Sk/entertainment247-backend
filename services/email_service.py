import os
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage 

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


# OTP Email
def sent_otp_email(email:str,otp:str):

    message = EmailMessage()
    message["Subject"] = "Entertainment 24/7 Password Reset Verification Code"
    message["From"] = f"Entertainment 24/7 <{EMAIL_ADDRESS}>"
    message["To"] = email

    message.set_content(
        f"""
Hello,

We received a request to reset the password for your Entertainment 24/7 account.

**Your One-Time Password (OTP) is:**

{otp}

This OTP is valid for **5 minutes**. For your security, please do not share this code with anyone.

If you did not request a password reset, you can safely ignore this email. Your account will remain secure, and no changes will be made without OTP verification.

If you continue to receive unexpected password reset requests, we recommend reviewing your account security.

Thank you for choosing **Entertainment 24/7**.

Best regards,
**Entertainment 24/7 Team**


""" )
    
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
        smtp.send_message(message)






# Welcome Email
def welcome_email(user_name:str,email:str,role:str):

    letter = EmailMessage()
   
    letter["To"] = email
    letter["From"] = f"Entertainment 24/7 <{EMAIL_ADDRESS}>"

    if (role=="admin"):
        letter["Subject"] = "Welcome, Administrator – Entertainment 24/7"
        letter.set_content(f"""
Hello {user_name},

Congratulations! Your Administrator account for Entertainment 24/7 has been successfully activated.

As an administrator, you have elevated access to manage and maintain the platform. Your responsibilities may include:

👥 Managing user accounts and permissions.
🎮 Adding, updating, and removing game listings.
🎬 Managing movie content and platform updates.
📊 Monitoring platform activity and ensuring a smooth user experience.
🔒 Maintaining the security and integrity of the platform.

Please use your administrative privileges responsibly and keep your account credentials secure. Never share your login details or verification codes with anyone.

If you believe you received this email in error or did not expect administrator access, please contact the system owner or support team immediately.

Thank you for helping us make Entertainment 24/7 the best destination for gaming and entertainment.

Best regards,

Entertainment 24/7 Team

""")
    else:
        letter["Subject"] = "Welcome to Entertainment 24/7 – Your Entertainment Journey Starts Here!"
        letter.set_content(f"""
Hello {user_name},

Welcome to Entertainment 24/7! 🎉

We're excited to have you join our community of gamers and movie enthusiasts.

Your account has been created successfully, and you're now ready to explore a world of entertainment—all in one place.

Here's what you can do with your account:

🎮 Discover and explore a wide collection of games.
🎬 Browse the latest and trending movies.
⭐ Save your favorites and enjoy personalized recommendations.
🔔 Stay updated with new releases, exclusive content, and upcoming features.

Your adventure starts now, and we're committed to bringing you the best gaming and movie experience.

If you have any questions or need assistance, our support team is always here to help.

Thank you for choosing Entertainment 24/7. We hope you enjoy every moment with us!

Happy Gaming & Happy Watching!

Warm regards,
The Entertainment 24/7 Team

""")
    
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
        smtp.send_message(letter)







# Password Changed Email
def sent_password_change_email(email:str):

    message = EmailMessage()
    message["Subject"] = "Entertainment 24/7 Password Changed Successfully"
    message["From"] = f"Entertainment 24/7 <{EMAIL_ADDRESS}>"
    message["To"] = email

    message.set_content(
        f"""
Subject: Password Changed Successfully

Dear User,

Your password for your Entertainment 24/7 account has been changed successfully.

If you made this change, no further action is required.

If you did not change your password, please contact our support team immediately and secure your account as soon as possible.

Thank you for choosing Entertainment 24/7.

Best regards,
Entertainment 24/7 Team


""" )
    
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
        smtp.send_message(message)
        

    