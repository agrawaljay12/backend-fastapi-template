import os 
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()


MAIL_USERNAME = os.getenv("MAIL_USERNAME")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
MAIL_PORT = int(os.getenv("MAIL_PORT"))
MAIL_SERVER = os.getenv("MAIL_SERVER")
MAIL_TLS = os.getenv("MAIL_TLS") == "True"
MAIL_SSL = os.getenv("MAIL_SSL") == "True"


def send_email(to_email:str, subject:str, body:str):

    try:
        msg = EmailMessage()
        msg['From'] = MAIL_USERNAME
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.set_content(body)

        if MAIL_SSL:
            server = smtplib.SMTP_SSL(MAIL_SERVER, MAIL_PORT)
        else:
            server = smtplib.SMTP(MAIL_SERVER, MAIL_PORT)
            if MAIL_TLS:
                server.starttls()

        server.login(MAIL_USERNAME, MAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
    except Exception as e:
        print(f"Error sending email: {e}")
