import requests
import os
from datetime import datetime
from twilio.rest import Client
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "69f04e4613056b159c2761a9d9e664d2"

account_sid = "ACf82b29f3718ba711a9e53f9e7bb836ca"
account_auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

print(account_auth_token)
client = Client(username=account_sid, password=account_auth_token)

weather_parameters = {
    "lat": 18.520430,
    "lon": 73.856743,
    "appid": api_key
}

response = requests.get(url=OWM_ENDPOINT, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
will_rain = False
time_now = datetime.now()

for forecast in weather_data["list"][0:4]:
    time_in_forecast = datetime.fromtimestamp(forecast["dt"])
    if time_in_forecast > time_now:
        if forecast["weather"][0]["id"] < 700:
            will_rain = True
        break

if will_rain:
    message = client.messages.create(
        body="Looks like it's going to rain today! Don't forget to bring an ☔",
        from_="+18145264325",
        to="+919795678808"
    )
    print(message.status)
