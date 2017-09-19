from sanic import Blueprint
from sanic.response import json,text
from module.mongo import PosData
from module.compute import block_check,getrecentcar_parallel 

posData = PosData()
api = Blueprint('api')

@api.route('/car/<car>')
async def findCar(request,car):
    try:
        dbCar = posData.getlastcar(int(car))[0]
    except:
        return json({'message':'dont have this car'})
    return json({'car':dbCar.get('car'),'X':dbCar.get('X'),'Y':dbCar.get('Y'),'V':dbCar.get('V'),'time':dbCar.get('time')})

@api.route('/cars')
async def findCar(request):
    Car = block_check(getrecentcar_parallel())
    return text(Car)
