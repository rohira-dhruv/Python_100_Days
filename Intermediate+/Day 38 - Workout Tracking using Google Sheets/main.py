import requests
import os
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 71
HEIGHT_CM = 183
AGE = 21

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
SHEETY_BEARER_TOKEN = os.environ.get("SHEETY_BEARER_TOKEN")
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
input_query = input("Tell me about the exercise you did?: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
    "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}"
}

exercise_params = {
    "query": input_query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
exercise_data_list = response.json()["exercises"]
today_date = datetime.now()

sheet_headers = {
    "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}"
}

for exercise in exercise_data_list:
    record_params = {
        "workout": {
            "date": today_date.strftime("%d/%m/%Y"),
            "time": today_date.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": round(float(exercise["duration_min"])),
            "calories": round(float(exercise["nf_calories"]))
        }
    }
    response = requests.post(url=SHEET_ENDPOINT, json=record_params, headers=sheet_headers)
    print(response.text)

