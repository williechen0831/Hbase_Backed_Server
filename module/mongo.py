"""moudule for mongodb query"""
import datetime
from conf.db_conf import client


class PosData:
    def __init__(self):
        db = client['BackendServer']
        self.col = db['posData']

    def update(self, car, x, y, vector):
        raw = {
            "car": int(car),
            "X": x,
            "Y": y,
            "V": vector,
            "time": datetime.datetime.now()
        }
        self.col.insert_one(raw)
        client.close()
        return True

    def getlastcar(self, car):
        raw = {
            "car": int(car)
        }
        return self.col.find(raw).sort('_id', -1)
