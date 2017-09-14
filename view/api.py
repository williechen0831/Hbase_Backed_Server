from sanic import Blueprint
from sanic.response import json
from module.mongo import PosData

posData = PosData()
api = Blueprint('api')

@api.route('/car/<car>')
async def findCar(request,car):
    dbCar = posData.getlastcar(int(car))
    return json({'car':dbCar.get('car'),'X':dbCar.get('X'),'Y':dbCar.get('Y'),'V':dbCar.get('V'),'time':dbCar.get('time')})
