from amadeus import Client, ResponseError, Location
from skyscanner.skyscanner import Flights
import http.client, json


class HermesFlights:
    flights_service = None

    def createClient(self):
        conn = http.client.HTTPSConnection("skyscanner-skyscanner-flight-search-v1.p.rapidapi.com")
        payload = "cabinClass=business&children=0&infants=0&country=US&currency=USD&locale=en-US&originPlace=SFO-sky&destinationPlace=LHR-sky&outboundDate=2019-10-20&adults=1"
        headers = {
            'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
            'x-rapidapi-key': "e68920b6ccmshe9f94cc47979710p113539jsn7f754a0867ec",
            'content-type': "application/x-www-form-urlencoded"
        }
        conn.request("POST", "/apiservices/pricing/v1.0", payload, headers)
        res = conn.getresponse()
        data = res.read()
        # print(data.decode("utf-8"))

    def getFlightData(self, origin, startDate):
        master = []
        conn = http.client.HTTPSConnection("skyscanner-skyscanner-flight-search-v1.p.rapidapi.com")
        headers = {
            'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
            'x-rapidapi-key': "e68920b6ccmshe9f94cc47979710p113539jsn7f754a0867ec"
        }
        conn.request("GET", "/apiservices/browsequotes/v1.0/US/USD/en-US/" + origin + "/Everywhere/" + startDate,
                     headers=headers)
        res = conn.getresponse()
        data = res.read()
        json_data = json.loads(data.decode("utf-8"))
        flightID = self.mapIdToLocation(json_data["Places"])
        # print(json_data["Quotes"])
        for flight in json_data["Quotes"]:
           master.append(self.getRelevantFlightInfo(flight, flightID))
        return json.dumps(master)

    def mapIdToLocation(self, data):
        flightID = {}
        for place in data:
            placeID = place["PlaceId"]
            country = place["Name"]
            flightID[placeID] = country
        return flightID

    def getRelevantFlightInfo(self, data, flightID):
        singleFlight = {}
        outboundLeg = data["OutboundLeg"]
        singleFlight["Price"] = data["MinPrice"]
        countryID = outboundLeg["DestinationId"]
        singleFlight["Place"] = flightID[countryID]
        singleFlight["DepartureDate"] = outboundLeg["DepartureDate"][0:10]
        singleFlight["DirectFlight"] = str(data["Direct"])
        return singleFlight

    def countryToTag(self, country):
        return 0

# flights = HermesFlights()
# flights.createClient()
# flights.getFlightData("BUF-sky", "2019-10-23")
