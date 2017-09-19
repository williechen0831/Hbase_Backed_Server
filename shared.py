import datetime
def gettrangecar(intCar):    
    db = client['BackendServer']
    col = db['posData']
    nowTime = datetime.datetime.now()
    deltaTime = datetime.timedelta(seconds=3)
    calcTime = nowTime - deltaTime
    raw = {
            "car":int(intCar),
            "time":
            {
                "$gte":calcTime,"$lte":nowTime
                }
            }
    return col.find(raw).sort('_id',-1)[0]

