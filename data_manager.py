import requests

class DataManager:

    def __init__(self):
        self.sheety_url = "https://api.sheety.co/cd25bffb434ffa9714c3610ed74dbb3b/copyOfFlightDeals/prices"
        response = requests.get(url=self.sheety_url)
        self.result = response.json()
        self.sheet_data = self.result["prices"]

    def update_iatacode(self, flight):
        for each_city in flight:
            id = each_city["id"]
            each_city = {
                "price": {
                    "city": each_city["city"],
                    "iataCode": each_city["iataCode"],
                    "id": each_city["id"],
                    "lowestPrice": each_city["lowestPrice"],
                }
            }
            updated_response = requests.put(url=f"{self.sheety_url}/{id}", json=each_city)
            self.updated_results = updated_response.json()
