import math
import geopy.distance
import datetime
from conf.dask_conf import client
import shared

def block_check(rawList):
    six_raw_list = []
    six_other_list = []
    for x in range(1,7):
        six_raw_list.append((float(rawList[0].get('X')),float(rawList[0].get('Y'))))
        six_other_list.append((float(rawList[x].get('X')),float(rawList[x].get('Y'))))
    listcompass = client.gather(client.map(shared.compass,six_raw_list,six_other_list))
    listdis = client.gather(client.map(shared.distance,six_raw_list,six_other_list))
    return listcompass

def block_check_1(rawList):
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
