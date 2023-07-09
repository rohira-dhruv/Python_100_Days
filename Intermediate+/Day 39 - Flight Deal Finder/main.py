from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notif_manager = NotificationManager()
ORIGIN_CITY_IATA = "LON"

if flight_data[0]["iataCode"] == "":
    for row in flight_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = flight_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in flight_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight.price < destination["lowestPrice"]:
        notif_manager.send_message(flight.price, flight.origin_city, flight.origin_airport, flight.destination_city,
                                   flight.destination_airport, flight.out_date, flight.return_date)
        break
