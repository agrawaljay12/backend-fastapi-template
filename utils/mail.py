import os 
# import smtplib
# from email.message import EmailMessage
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import logging

# load the environment variable 
if("ENVIRONMENT")=="development":
    load_dotenv(".env.development")
else:
    load_dotenv()

MAIL_USERNAME = os.getenv("MAIL_USERNAME")
SENDGRID_API_KEY =os.getenv("SENDGRID_API_KEY")

# send the mail using sendgrid service
def send_email(to_email:str, subject:str, body:str):
    try:

        msg = Mail(
            from_email=MAIL_USERNAME,
            to_emails=to_email,
            subject=subject,
            html_content=body
        )
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(msg)

        logging.info(f"Email sent to {to_email}")

        return response
    except Exception as e:
        logging.info(f"failed to send mail:{str(e)}")
        

# MAIL_USERNAME = os.getenv("MAIL_USERNAME")
# MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
# MAIL_PORT = int(os.getenv("MAIL_PORT"))
# MAIL_SERVER = os.getenv("MAIL_SERVER")
# MAIL_TLS = os.getenv("MAIL_TLS") == "True"
# MAIL_SSL = os.getenv("MAIL_SSL") == "True"

# def send_email(to_email:str, subject:str, body:str):

#     try:
#         msg = EmailMessage()
#         msg['From'] = MAIL_USERNAME
#         msg['To'] = to_email
#         msg['Subject'] = subject

#         msg.set_content(body)

#         if MAIL_SSL:
#             server = smtplib.SMTP_SSL(MAIL_SERVER, MAIL_PORT)
#         else:
#             server = smtplib.SMTP(MAIL_SERVER, MAIL_PORT)
#             if MAIL_TLS:
#                 server.starttls()

#         server.login(MAIL_USERNAME, MAIL_PASSWORD)
#         server.send_message(msg)
#         server.quit()
#     except Exception as e:
#         print(f"Error sending email: {e}")
