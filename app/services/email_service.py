import os
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from dotenv import load_dotenv

load_dotenv()


def send_email(subject: str, body: str):

    sender = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_PASSWORD")
    receiver = os.getenv("OWNER_EMAIL")

    if not sender or not password or not receiver:
        return {
            "success": False,
            "message": "Email credentials not configured."
        }

    try:

        message = MIMEMultipart()

        message["From"] = sender
        message["To"] = receiver
        message["Subject"] = subject

        message.attach(
            MIMEText(body, "plain")
        )

        with smtplib.SMTP("smtp.gmail.com", 587) as server:

            server.starttls()

            server.login(
                sender,
                password,
            )

            server.sendmail(
                sender,
                receiver,
                message.as_string(),
            )

        return {
            "success": True,
            "message": "Email sent successfully."
        }

    except Exception as e:

        return {
            "success": False,
            "message": str(e)
        }