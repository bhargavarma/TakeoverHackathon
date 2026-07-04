import smtplib
import os

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(
    recipient: str,
    subject: str,
    body: str,
):
    """
    Sends an email notification.
    """

    sender = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_PASSWORD")

    if not sender or not password:
        return {
            "status": "Email credentials not configured."
        }

    try:

        message = MIMEMultipart()

        message["From"] = sender
        message["To"] = recipient
        message["Subject"] = subject

        message.attach(
            MIMEText(body, "plain")
        )

        server = smtplib.SMTP(
            "smtp.gmail.com",
            587,
        )

        server.starttls()

        server.login(
            sender,
            password,
        )

        server.send_message(message)

        server.quit()

        return {
            "status": "Email sent successfully."
        }

    except Exception as e:

        return {
            "status": "Email failed.",
            "error": str(e),
        }


def send_whatsapp(
    phone_number: str,
    message: str,
):
    """
    Placeholder.

    Tomorrow we will connect
    Twilio WhatsApp API.
    """

    return {
        "status": "WhatsApp service not connected yet.",
        "phone": phone_number,
        "message": message,
    }