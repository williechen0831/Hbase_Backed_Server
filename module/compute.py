"""module of dask compute"""
import json
from conf.dask_conf import client
import shared

def block_check(listRaw):
    """function block check dask compute"""
    listSixraw = []
    listSixother = []
    for x in range(1, 7):
        if listRaw[0] is not None:
            listSixraw.append((float(listRaw[0].get('X')), float(listRaw[0].get('Y'))))
        else:
            listSixraw.append((0, 0))

        if listRaw[x] is not None:
            listSixother.append((float(listRaw[x].get('X')), float(listRaw[x].get('Y'))))
        else:
            listSixother.append((0, 0))

    listCompass = client.gather(client.map(shared.compass_calc, listSixraw, listSixother))
    listDis = client.gather(client.map(shared.distance_calc, listSixraw, listSixother))
    listBlock = client.gather(client.map(shared.block_calc, listCompass, listDis))
    vData = 0
    if listRaw[0] is None:
        vData = 0
    else:
        vData = float(listRaw[0].get('V'))
    return {
        'listBlock':json.dumps(listBlock),
        'listDis':json.dumps(listDis),
        'vData':json.dumps(vData),
        'sData':json.dumps(2)
        }


def getrecentcar_parallel():
    """function of recent car compute"""
    carsObj = client.gather(client.map(shared.gettrangecar, range(7)))
    return carsObj
