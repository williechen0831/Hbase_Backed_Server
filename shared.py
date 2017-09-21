"""compute shared module"""
import datetime
import math

# src :https://gist.github.com/jeromer/2005586
def compass_calc(pointA, pointB):
    """function of compass calulator """
    floatLat1dis = math.radians(pointA[0])
    floatLat2dis = math.radians(pointB[0])
    floatDifflong = math.radians(pointB[1] - pointB[1])
    axisX = math.sin(floatDifflong) * math.cos(floatLat2dis)
    axisY = math.cos(floatLat1dis) * math.sin(floatLat2dis) - (
        math.sin(floatLat1dis)* math.cos(floatLat2dis) * math.cos(floatDifflong))
    initial_bearing = math.atan2(axisX, axisY)
    initial_bearing = math.degrees(initial_bearing)
    compass_bearing = (initial_bearing + 360) % 360
    return compass_bearing

def distance_calc(pointA, pointB):
    """function of distance calulator"""
    intRadius = 6371 # km
    floatLatdis = math.radians(pointB[0]-pointA[0])
    floatLondis = math.radians(pointB[1]-pointA[1])
    floatA = math.sin(floatLatdis/2) * math.sin(floatLatdis/2) + math.cos(math.radians(pointA[0])) \
        * math.cos(math.radians(pointB[0])) * math.sin(floatLondis/2) * math.sin(floatLondis/2)
    floatC = 2 * math.atan2(math.sqrt(floatA), math.sqrt(1-floatA))
    floatDistance = intRadius * floatC
    return floatDistance * 1000

def determine_calc(angle):
    """function of largest distance angle"""
    return abs(1.875/math.cos(angle))

def block_calc(floatAngle, floatDistance):
    """function of block compute"""
    intAngle = int(floatAngle)
    if intAngle >= 0 and intAngle < 90:
        if floatDistance < determine_calc(intAngle):
            ans_of_return = 2
        else:
            ans_of_return = 3
    if intAngle >= 90 and intAngle < 180:
        if intAngle == 90:
            ans_of_return = 6
        elif floatDistance < determine_calc(intAngle):
            ans_of_return = 5
        else:
            ans_of_return = 6
    if intAngle >= 180 and intAngle < 270:
        if floatDistance < determine_calc(intAngle):
            ans_of_return = 5
        else:
            ans_of_return = 4
    if intAngle >= 270 and intAngle < 360:
        if intAngle == 270:
            ans_of_return = 4
        elif floatDistance < determine_calc(intAngle):
            ans_of_return = 2
        else:
            ans_of_return = 1
    return ans_of_return

def gettrangecar(intCar):
    """function of getrange of car compute"""
    db = client['BackendServer']
    col = db['posData-test']
    timeNow = datetime.datetime.now()
    timeDelta = datetime.timedelta(seconds=3)
    timeCalc = timeNow - timeDelta
    raw = {
        "car":int(intCar),
        "time":
            {
                "$gte":timeCalc, "$lte":timeNow
                }
        }
    returnValue = []
    if col.find(raw).sort('_id', -1).count() == 0:
        returnValue = None
    else:
        returnValue = col.find(raw).sort('_id', -1)[0]
    return returnValue
