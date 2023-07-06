import time
import requests
from datetime import datetime, timezone
import smtplib
# INSERT YOUR CREDENTIALS HERE.
MY_LAT = -40
MY_LONG = 110
MY_EMAIL = "gl1tch.djr@gmail.com"
MY_PASSWORD = "yhdyslduogyvrxxs"


def is_iss_close():
    response_latlng = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_latlng.raise_for_status()
    data_latlng = response_latlng.json()

    iss_latitude = float(data_latlng["iss_position"]["latitude"])
    iss_longitude = float(data_latlng["iss_position"]["longitude"])
    print(iss_latitude, iss_longitude)
    print(MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5)
    return MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now(tz=timezone.utc).hour
    print(sunrise, sunset, time_now)
    print(time_now > sunset or time_now < sunrise)
    return time_now > sunset or time_now < sunrise


while True:
    if is_iss_close() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject: Look Up\n\nThe ISS is above you in the sky."
            )
            print("Mail Sent")
            break
    time.sleep(60)
