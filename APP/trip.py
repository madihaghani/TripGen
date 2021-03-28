import location
import os
import constants
import requests
import json
from location import Location

class Trip(Location):
    def __init__(self, *locations):
        self.places = [Location(location).set_attributes(location) for location in locations]



    # def __from_locations__(self):
    #     # for location in self.locations:
    #     pass

    def generate_trip(self):
        result = []
        for i, place in enumerate(self.places):
            if i < len(self.places)-1:
                print(place, Location(place))
                latitude1, longitude1 = place[:2]
                latitude2, longitude2 = self.places[i+1][:2]
                _coordinates = latitude1 + ',' + longitude1 + ':' + latitude2 + ',' + longitude2
                _path = os.path.join(constants.TOMTOM_ROUTING_API_URL, _coordinates +
                                     constants.TOMTOM_ROUTING_FORMAT + constants.TOMTOM_API_KEY)
                print(_path)

                # _response = requests.get(_path)
                # _json_data = json.loads(_response.text)
                # print(_json_data)




# https://api.tomtom.com/routing/1/calculateRoute/52.50931%2C13.42936%3A52.50274%2C13.43872/json?avoid=unpavedRoads&key=*****
if __name__ == '__main__':
    trip = Trip('new york , ny ', 'boston, ma ', 'washington, dc')
    print(trip.places)
    print(trip.generate_trip())
