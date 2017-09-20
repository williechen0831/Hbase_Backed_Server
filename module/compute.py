from conf.dask_conf import client
import shared
import json

def block_check(rawList):
    six_raw_list = []
    six_other_list = []
    for x in range(1,7):
        if rawList[0] is not None:
            six_raw_list.append((float(rawList[0].get('X')),float(rawList[0].get('Y'))))
        else:
            six_raw_list.append((0,0))

        if rawList[x] is not None:
            six_other_list.append((float(rawList[x].get('X')),float(rawList[x].get('Y'))))
        else:
            six_other_list.append((0,0))

    listCompass = client.gather(client.map(shared.compass,six_raw_list,six_other_list))
    listDis = client.gather(client.map(shared.distance,six_raw_list,six_other_list))
    listBlock = client.gather(client.map(shared.block,listCompass,listDis))
    vData = 0
    if rawList[0] is None :
        vData = 0
    else:
        vData = float(rawList[0].get('V'))
    return {'listBlock':json.dumps(listBlock),'listDis':json.dumps(listDis),"vData":json.dumps(vData),"sData":json.dumps(2)}


def getrecentcar_parallel():
    carsObj = client.gather(client.map(shared.gettrangecar,range(7)))
    return carsObj
