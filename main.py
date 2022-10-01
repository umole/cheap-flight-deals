#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from pprint import pprint
from flight_data import FlightData


data_manager = DataManager()
#flight_search = FlightSearch()
#updated_sheet = data_manager.update_iatacode()
sheet_data = data_manager.get_destination_data()

price = ""
city_from = ""
city_to = ""

if sheet_data[0]['iataCode'] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row['iataCode'] = flight_search.get_destination_code(row['city'])
    pprint(sheet_data)

    data_manager.destination_data = sheet_data
    update_data = data_manager.update_iatacode()

flight_data = FlightData()
flights = flight_data.search_for_cheap_flights()
for trip in flights:
    price = trip['price']
    city_from = trip['cityFrom']
    city_to = trip['cityTo']
    flight_time = trip['local_departure'].split("T", 1)[0]
    #split_time = flight_time.split("T")

    print(f"{price} EUR, from {city_from}, to  {city_to}. {flight_time}")
#pprint(flights)


