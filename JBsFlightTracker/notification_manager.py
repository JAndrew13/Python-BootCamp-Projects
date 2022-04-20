import smtplib

EMAIL_PROVIDER_SMPT_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "pythonpal29@gmail.com"
MY_PASSWORD = "122191Jb0*"

from twilio.rest import Client

TWILIO_SID = "AC257d050c42d67514c1abc1f49677cee8"
TWILIO_AUTH_TOKEN = "d505e624214999b29ea278b21830ca25"
TWILIO_VIRTUAL_NUMBER = "+14842710093"
TWILIO_VERIFIED_NUMBER = "+17138284622"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(EMAIL_PROVIDER_SMPT_ADDRESS, port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )
