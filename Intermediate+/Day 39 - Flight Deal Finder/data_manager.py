import os
import requests
SHEETY_PRICES_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")


class DataManager:

    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        sheet_response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        sheet_response.raise_for_status()
        data = sheet_response.json()
        self.destination_data = data["deals"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "deal": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", json=new_data)
            response.raise_for_status()
            print(response.text)
