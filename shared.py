import datetime
def gettrangecar(intCar,intSec):    
    db = client['BackendServer']
    col = db['posData']
    nowTime = datetime.datetime.now()
    deltaTime = datetime.timedelta(seconds=int(intSec))
    calcTime = nowTime - deltaTime
    raw = {
            "car":int(intCar),
            "time":
            {
                "$gte":calcTime,"$lte":nowTime
                }
            }
    return col.find(raw).sort('_id',-1)[0]

