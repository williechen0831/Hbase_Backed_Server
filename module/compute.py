import math
import geopy.distance
import datetime
from conf.dask_conf import client
import shared
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

def distance(pointA,pointB):
    return geopy.distance.vincenty(pointA, pointB).km

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

def block_check(rawList):
    listcompass = []
    listdis = []
    listblock = []
    for x in range(1,6):
        listdis.append(
                distance((float(rawList[0].get('X')),float(rawList[0].get('Y'))),(float(rawList[x].get('X')),float(rawList[x].get('Y')))))
        listcompass.append(
                compass((float(rawList[0].get('X')),float(rawList[0].get('Y'))),(float(rawList[x].get('X')),float(rawList[x].get('Y')))))
    u = 0
    for x in listcompass:
        listblock.append(block(x,listdis[u]))
        u = u + 1


    return listblock

def getrecentcar_parallel():
    carsObj = client.gather(client.map(shared.gettrangecar,range(7)))
    return carsObj
