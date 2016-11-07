from geopy.geocoders import Nominatim

def verify_distance():

    geolocator = Nominatim()
    location = geolocator.geocode("94538")
    print (location.address)
    print (location.latitude)
    print (location.longitude)

    # loc1 = [-73.88648210000001, 40.5666985]
    # loc2 = [-73.93414657, 40.82302903]
    # loc1 = [-73.01, 40]
    # loc2 = [-73, 40.01]
    # m = vincenty(loc2, loc1).miles
    # k = vincenty(loc2, loc1)
    # print m
    # print m.__class__
    return False

def main():

    print (verify_distance())

if __name__ == '__main__':
    main()
