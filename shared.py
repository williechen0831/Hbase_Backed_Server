"""compute shared module"""
import datetime
import math

# src :https://gist.github.com/jeromer/2005586


def compass_calc(pointA, pointB):
    """function of compass calulator """
    if pointB[0] == 0 and pointB[0] == 0:
        pointA = (0, 0)
    floatLat1dis = math.radians(pointA[0])
    floatLat2dis = math.radians(pointB[0])
    floatDifflong = math.radians(pointB[1] - pointA[1])
    axisX = math.sin(floatDifflong) * math.cos(floatLat2dis)
    axisY = math.cos(floatLat1dis) * math.sin(floatLat2dis) - (
        math.sin(floatLat1dis) * math.cos(floatLat2dis) * math.cos(floatDifflong))
    initial_bearing = math.atan2(axisX, axisY)
    initial_bearing = math.degrees(initial_bearing)
    compass_bearing = (initial_bearing + 360) % 360
    return compass_bearing


def distance_calc(pointA, pointB):
    """function of distance calulator"""
    if pointB[0] == 0 and pointB[0] == 0:
        pointA = (0, 0)
    intRadius = 6371  # km
    floatLatdis = math.radians(pointB[0] - pointA[0])
    floatLondis = math.radians(pointB[1] - pointA[1])
    floatA = math.sin(floatLatdis / 2) * math.sin(floatLatdis / 2) \
            + math.cos(math.radians(pointA[0])) * math.cos(math.radians(pointB[0])) \
            * math.sin(floatLondis / 2) * math.sin(floatLondis / 2)
    floatC = 2 * math.atan2(math.sqrt(floatA), math.sqrt(1 - floatA))
    floatDistance = intRadius * floatC
    return floatDistance * 1000


def determine_calc(angle):
    """function of largest distance angle"""
    return abs(1.875 / math.cos(angle))


def block_calc(floatAngle, floatDistance):
    """function of block compute"""
    if floatAngle > 0 and floatAngle < 90:
        if floatDistance < determine_calc(floatAngle):
            ans_of_return = 2
        else:
            ans_of_return = 3
    if floatAngle > 90 and floatAngle < 180:
        if floatDistance < determine_calc(floatAngle):
            ans_of_return = 5
        else:
            ans_of_return = 6
    if floatAngle > 180 and floatAngle < 270:
        if floatDistance < determine_calc(floatAngle):
            ans_of_return = 5
        else:
            ans_of_return = 4
    if floatAngle > 270 and floatAngle < 360:
        if floatDistance < determine_calc(floatAngle):
            ans_of_return = 2
        else:
            ans_of_return = 1
    if floatAngle == 90:
        ans_of_return = 6
    if floatAngle == 180:
        ans_of_return = 5
    if floatAngle == 270:
        ans_of_return = 4
    if floatAngle == 0:
        ans_of_return = 2
    return ans_of_return


def gettrangecar(intCar):
    """function of getrange of car compute"""
    db = client['BackendServer']
    col = db['posData']
    timeNow = datetime.datetime.now()
    timeDelta = datetime.timedelta(seconds=3)
    timeCalc = timeNow - timeDelta
    raw = {
        "car": int(intCar),
        "time":
            {
                "$gte": timeCalc, "$lte": timeNow
                }
    }
    returnValue = []
    if col.find(raw).sort('_id', -1).count() == 0:
        returnValue = None
    else:
        returnValue = col.find(raw).sort('_id', -1)[0]
    return returnValue
