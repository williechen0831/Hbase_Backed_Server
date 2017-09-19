from conf.db_conf import client
import datetime

class PosData:
    def __init__(self):
        db = client['BackendServer']
        self.col = db['posData']

    def update(self,car,x,y,vector):
        raw = {
                "car":int(car),
                "X":x,
                "Y":y,
                "V":vector,
                "time":datetime.datetime.now()
                }
        self.col.insert_one(raw)
        client.close()
        return True

    def getlastcar(self,car):
        raw = {
                "car":int(car)
                }
        return self.col.find(raw).sort('_id',-1)

def gettrangecar(intCar):
    return intCar
        #db = client['BackendServer']
        #col = db['posData']
        #nowTime = datetime.datetime.now()
        #deltaTime = datetime.timedelta(seconds=int(intSec))
        #calcTime = nowTime - deltaTime
"""
        raw = {
                "car":int(intCar),
                "time":
                {
                    "$gte":calcTime,"$lte":nowTime
                }
            }
"""


class LedData:
    def __init__(self):
        self.col = db['ledData']
