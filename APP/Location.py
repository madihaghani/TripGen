import requests
import constants
import os
import json

class Location:
    def __init__(self, query):
        self.query = query
        self.latitude, self.longitude, self.address = self.set_attributes(self.query)

    @staticmethod
    def set_attributes(query):
        #https://api.tomtom.com/search/2/geocode/Saginaw%20MI.json?&key=*****
        _PATH = os.path.join(constants.TOMTOM_API_URL, query + constants.EXTENSION + constants.TOMTOM_API_KEY)
        _response = requests.get(_PATH)
        _json_data = json.loads(_response.text)
        print(_json_data)
        return _json_data['results'][0]['position']['lat'], \
               _json_data['results'][0]['position']['lon'], \
               _json_data['results'][0]['address']['freeformAddress']

    def __str__(self):
        return self.address






if __name__ == '__main__':
    loc = Location('university of chicago')
    print(loc.latitude)
    print(loc.longitude)
    print(loc.address)
    print(loc)