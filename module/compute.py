import math
import geopy.distance
import datetime
from conf.dask_conf import client
import shared

def block_check(rawList):
    six_list = []
    for x in range(0,5):
        six_list.append((float(rawList[0].get('X')),float(rawList[0].get('Y'))))
    listcompass = client.gather(client.map(shared.compass,six_list,(float(rawList[range(1,7)].get('X')),float(rawList[range(1,7)].get('Y')))))
    return listcompass

def block_check(rawList):
    listcompass = []
    listdis = []
    listblock = []
    for x in rawList:
        listdis.append(
                distance((float(rawList[0].get('X')),float(rawList[0].get('Y'))),(float(x.get('X')),float(x.get('Y'))))*1000)
        listcompass.append(
                compass((float(rawList[0].get('X')),float(rawList[0].get('Y'))),(float(x.get('X')),float(x.get('Y')))))
    u = 0
    for x in listcompass:
        listblock.append(block(x,listdis[u]))
        u = u + 1


    return listblock

def getrecentcar_parallel():
    carsObj = client.gather(client.map(shared.gettrangecar,range(7)))
    return carsObj
