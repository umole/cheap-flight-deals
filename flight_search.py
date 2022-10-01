import requests

from data_manager import DataManager

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = "07Xwr8MArsKJh7F3S-gBYGfWhfmhymTV"


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        location_url = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {
            "apikey": TEQUILA_API_KEY
        }
        query = {
            "term": city_name,
            "location_types": "airport",
        }
        response = requests.get(url=location_url, headers=headers, params=query)
        flight_search_result = response.json()
        flight_location = flight_search_result['locations']
        code = flight_location[0]['code']
        return code

