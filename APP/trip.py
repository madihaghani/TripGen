import location
from location import Location

class Trip(Location):
    def __init__(self, *locations):
        self.locations = locations
        self.places = list()

    def __from_locations__(self):
        # for location in self.locations:
        pass



if __name__ == '__main__':
    trip = Trip('new york , ny ', 'boston, ma ', 'washington, dc')
    print(trip.locations)
