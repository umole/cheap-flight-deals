import requests
from pprint import pprint

SHEETY_API_URL = "https://api.sheety.co/cd25bffb434ffa9714c3610ed74dbb3b/copyOfFlightDeals/prices"

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        sheety_url = SHEETY_API_URL
        response = requests.get(url=sheety_url)
        result = response.json()
        self.destination_data = result["prices"]
        return self.destination_data

    def update_iatacode(self):
        for each_city in self.destination_data:
            id = each_city["id"]
            body = {
                "price": {
                    "iataCode": each_city['iataCode'],
                   # "id": each_city["id"],
                   # "lowestPrice": each_city["lowestPrice"],
                }
            }
            updated_response = requests.put(url=f"{SHEETY_API_URL}/{id}", json=body)
            self.updated_results = updated_response.json()
