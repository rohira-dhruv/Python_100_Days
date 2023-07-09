import os
from twilio.rest import Client
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = "+18145264325"


class NotificationManager:

    def send_message(self, price, origin_city, origin_airport, destination_city, destination_airport, from_date, to_date):
        client = Client(username=TWILIO_ACCOUNT_SID, password=TWILIO_AUTH_TOKEN)
        client.messages.create(
            from_=TWILIO_PHONE_NUMBER,
            to="+916386932267",
            body=f"\nLow Price Alert! Only £{price} to fly from {origin_city}-{origin_airport} to {destination_city}-"
                 f"{destination_airport}, from {from_date} to {to_date}"
        )
