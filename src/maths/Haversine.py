from math import radians, cos, sin, asin, sqrt
import time

current_milli_time = lambda: int(round(time.time() * 1000))

def haversine(point1, point2, miles = False):

    AVG_EARTH_RADIUS = 6371

    lat1, lng1 = point1
    lat2, lng2 = point2

    # convert all latitudes/longitudes from decimal degrees to radians
    lat1, lng1, lat2, lng2 = map(radians, (lat1, lng1, lat2, lng2))

    # calculate haversine
    lat = lat2 - lat1
    lng = lng2 - lng1
    d = sin(lat * 0.5) ** 2 + cos(lat1) * cos(lat2) * sin(lng * 0.5) ** 2
    h = 2 * AVG_EARTH_RADIUS * asin(sqrt(d))
    if miles:
        return h * 0.621371  # in miles
    else:
        return h

    pass

def main():

    # lyon = (45.7597, 4.8422)
    # paris = (48.8567, 2.3508)
    lyon = (12.9210784, 77.6936946)  # Saroj
    paris = (12.9132164, 77.6234387)  # Snapwiz

    totalDelay = 0

    start = current_milli_time()
    for i in range(0,300000,1):
        # print i
        start = current_milli_time()
        dist = haversine(lyon, paris)
        end = current_milli_time()
        delay = start-end
        if delay > 0:
            totalDelay += delay

    end = current_milli_time()

    print end
    print start
    print "That's All. Total Delay: " + str(end-start)


    # time.sleep(5)
    # start = time.time()
    # print (haversine(lyon, paris, miles=True))
    # end = time.time()
    # print "%.20f" % start-end

    pass

if __name__ == '__main__':
    main()
