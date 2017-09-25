"""moudule for mongodb query"""
import datetime
from conf.db_conf import client
from pymongo.errors import CursorNotFound
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
        try:
            return self.col.find(raw).sort('_id', -1)
        except CursorNotFound:
            return 'Error'
