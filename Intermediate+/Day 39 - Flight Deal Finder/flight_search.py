import os
import requests
from flight_data import FlightData

KIWI_TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
KIWI_API_KEY = os.environ.get("KIWI_API_KEY")


class FlightSearch:

    def get_destination_code(self, city):
        locations_endpoint = f"{KIWI_TEQUILA_ENDPOINT}/locations/query"
        headers = {
            "apikey": KIWI_API_KEY
        }
        destination_params = {
            "term": city,
            "location_types": "city"
        }
        code_response = requests.get(url=locations_endpoint, headers=headers, params=destination_params)
        results = code_response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {
            "apikey": KIWI_API_KEY
        }
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "curr": "GBP",
            "max_stopovers": 0
        }

        response = requests.get(url=f"{KIWI_TEQUILA_ENDPOINT}/v2/search", headers=headers, params=query)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for destination {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        return flight_data
