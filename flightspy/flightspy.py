import requests
import json

headers = {'Content-Type': 'application/json'}
# TODO: Push to HEROKU and Improve. Allow users to search for location and IATA code
# TODO: Create a tool to run this each day for two weeks away and pull data into a database and track price changes.
# TODO: Look up more data work on GITHUB
class FlightsPy(object):
    """Class to be instantiated to use the script"""

    def __init__(self, key):
        self.URL = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key=%s'% key
        self.KEY = key
        self.request = None
        self.params = {}

    def grab(self, params):
        """Grabs flight data from Google API"""
        r = requests.post(self.URL, json={
            "request":{
                "slice": [
                    {"origin": params['origin'],
                     "destination": params['destination'],
                     "date": params['date']
                        },
                    ],
                "passengers": {
                    "adultCount": 1,
                    "infantInLapCount": 0,
                    "infantInSeatCount": 0,
                    "childCount": 0,
                    "seniorCount": 0
                    },
                "solutions": params['solutions'],
                "saleCountry": "US",
                "refundable": 'false'
                }
            }, headers = headers)

        self.request = r

        data = json.loads(r.text)

        self.data = data

        try:
            self.count = len(self.data['trips']['tripOption'])
        except:
            raise Exception(self.data)
        self.trips = self.data['trips']['tripOption']

    def print_trip(self, trip):
        Slice = 0
        for s in trip["slice"]:
            Slice +=  1
            print("   Slice %s" % Slice)
            for flight in s["segment"]:
                flight_number = flight["flight"]["number"]
                flight_carrier = flight["flight"]["carrier"]
                flight_origin = flight["leg"][0]["origin"]
                flight_departureTime = flight["leg"][0]["departureTime"]
                flight_destination = flight["leg"][0]["destination"]
                flight_arrivalTime = flight["leg"][0]["arrivalTime"]
                flight_mileage = flight["leg"][0]["mileage"]
                print("     %s%s %s %s %s %s  %s mileage"% (flight_carrier, flight_number, flight_origin, flight_departureTime, flight_destination, flight_arrivalTime, flight_mileage))

    def print_result(self):
        if self.trips != None:
            Solution = 0
            for trip in self.trips:
                Solution += 1
                print("\nSolution# %s Sale Price: %s" % (Solution, trip["saleTotal"]))
                self.print_trip(trip)
        else:
            print("No data yet")
