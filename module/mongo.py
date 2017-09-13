from conf.db_conf import client
import datetime
db = client['BackendServer']

class PosData:
    def __init__(self):
        self.col = db['posData']

    def update(self,car,x,y,vector):
        raw = {
                "car":int(car),
                "X":x,
                "Y":y,
                "V":vector,
                "time":datetime.datetime.utcnow()
                }
        self.col.insert_one(raw)
        return True

    def getlastcar(self,car):
        raw = {
                "car":int(car)
                }
        return self.col.find(raw).sort({$natural:1}).limit(1);

class LedData:
    def __init__(self):
        self.col = db['ledData']
