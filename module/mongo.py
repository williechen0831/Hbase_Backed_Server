from conf.db_conf import client
import datetime
db = client['BackendServer']

class PosData:
    def __init__(self):
        self.col = db['posData']

    def update(self,car,x,y,vector):
        raw = {
                "car":car,
                "X":x,
                "Y":y,
                "V":vector,
                "time":datetime.datetime.utcnow()
                }
        self.col.insert_one(raw)
        return True

class LedData:
    def __init__(self):
        self.col = db['ledData']
