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
                "time":datetime.datetime.utcnow()
                }
        self.col.insert_one(raw)
        client.close()
        return True

    def getlastcar(self,car):
        raw = {
                "car":int(car)
                }
        return self.col.find(raw).sort('_id',-1).limit(1);
    def getsixcar(self,time):
        datetimeNow = datetime.datetime.utcnow()
        delta = datetime.timedelta(seconds=int(time))
        seclater = datetimeNow - delta
        cars = {}
        for car in range(0,7):
            carNeed = self.col.find({car : car , time : {"gte":seclater,"lte":datetimeNow }}).sort('_id',-1).limit(1)
            print(carNeed[0])
            try:
                cars[car] = [carNeed[0].get('X'),carNeed[0].get('Y'),carNeed[0].get('X')]
            except:
                cars[car] = None
        return cars


class LedData:
    def __init__(self):
        self.col = db['ledData']
