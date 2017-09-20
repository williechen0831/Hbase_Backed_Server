from conf.dask_conf import client
import shared

def block_check(rawList):
    six_raw_list = []
    six_other_list = []
    for x in range(1,7):
        try:
            six_raw_list.append((float(rawList[0].get('X')),float(rawList[0].get('Y'))))
        except:
            six_raw_list.append((0,0))
        try:
            six_other_list.append((float(rawList[x].get('X')),float(rawList[x].get('Y'))))
        except:
            six_other_list.append((0,0))

    listCompass = client.gather(client.map(shared.compass,six_raw_list,six_other_list))
    listDis = client.gather(client.map(shared.distance,six_raw_list,six_other_list))
    listBlock = client.gather(client.map(shared.block,listCompass,listDis))
    return [listBlock,listDis,rawList[0].get('V')]


def getrecentcar_parallel():
    carsObj = client.gather(client.map(shared.gettrangecar,range(7)))
    return carsObj
