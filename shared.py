import datetime
import math
# src :https://gist.github.com/jeromer/2005586
def compass(pointA, pointB):
    lat1 = math.radians(pointA[0])
    lat2 = math.radians(pointB[0])
    diffLong = math.radians(pointB[1] - pointA[1])
    x = math.sin(diffLong) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1)
            * math.cos(lat2) * math.cos(diffLong))
    initial_bearing = math.atan2(x, y)
    initial_bearing = math.degrees(initial_bearing)
    compass_bearing = (initial_bearing + 360) % 360
    return compass_bearing

def distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # km
    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c
    return d * 1000

def determine(angle):
    return abs(1.875/math.cos(angle))

def block(angle,d):
    if angle>0 and angle<90:
        if d < determine(angle):
            return 2
        else:
            return 3
    if angle>90 and angle <180:
        if d < determine(angle):
            return 5
        else:
            return 6
    if angle>180 and angle <270:
        if d < determine(angle):
            return 5
        else:
            return 4
    if angle>270 and angle<360:
        if d < determine(angle):
            return 2
        else:
            return 1

def gettrangecar(intCar):
    db = client['BackendServer']
    col = db['posData-test']
    nowTime = datetime.datetime.now()
    deltaTime = datetime.timedelta(seconds=3)
    calcTime = nowTime - deltaTime
    raw = {
            "car":int(intCar),
            "time":
            {
                "$gte":calcTime,"$lte":nowTime
                }
            }
    returnValue = []
    if col.find(raw).sort('_id',-1).count() == 0:
        returnValue = None
    else:
        returnValue = col.find(raw).sort('_id',-1)[0]
    return returnValue

