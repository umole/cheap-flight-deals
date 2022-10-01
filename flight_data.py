import requests
import datetime
from data_manager import DataManager

FLIGHT_API_ENDPOINT = "https://api.tequila.kiwi.com/v2"
FLIGHT_API_KEY = "07Xwr8MArsKJh7F3S-gBYGfWhfmhymTV"

class FlightData:
    #This class is responsible for structuring the flight data.
    def search_for_cheap_flights(self):
        time = datetime.datetime.now()
        formatted_time = time.strftime("%d/%m/%Y")
        future_time = time + datetime.timedelta(days=30 * 6)
        header = {
            "apikey": FLIGHT_API_KEY
        }
        query = {
            "fly_from": "LOS",
            "date_from": formatted_time,
            "date_to": future_time.strftime("%d/%m/%Y")
        }
        response = requests.get(url=f"{FLIGHT_API_ENDPOINT}/search", headers=header, params=query)
        result = response.json()['data']
        return result
