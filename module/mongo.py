"""moudule for mongodb query"""
import datetime
from conf.db_conf import client
class PosData:
    """Position Data"""
    def __init__(self):
        db = client['BackendServer']
        self.col = db['posData']

    def update(self, car, x, y, vector):
        """update new car"""
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
        """last car get function"""
        raw = {
            "car": int(car)
        }
        if not self.col.find(raw).count() == 0:
            data = self.col.find(raw).sort('_id', -1)
        else:
            data = 'Error'
        return data
