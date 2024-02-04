import requests
import os
from datetime import datetime

from requests import HTTPError
from twilio.rest import Client

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "82ad81e2870e038b6093109da9a91702"

account_sid = os.environ.get("TWILIO_ACCOUNT_SSID")
account_auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

client = Client(username=account_sid, password=account_auth_token)

weather_parameters = {
    "lat": 18.520430,
    "lon": 73.856743,
    "appid": api_key
}

response = requests.get(url=OWM_ENDPOINT, params=weather_parameters)
try:
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
            from_="+16592347418",
            to="+916386932267"
        )
        print(message.status)
    else:
        print("Looks like it won't rain today.")

except HTTPError:
    print("Failed fetching response from the OpenWeatherMap API")
