#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch


flight_deals = DataManager()
iata = FlightSearch(flight_deals.sheet_data)
updated_sheet = flight_deals.update_iatacode(flight_deals.sheet_data)
pprint(flight_deals.sheet_data)


