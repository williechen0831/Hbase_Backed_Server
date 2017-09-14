from sanic import Blueprint
from sanic.response import json
from module.mongo import PosData

posData = PosData()
api = Blueprint('api')

@api.route('/car/<car>')
async def findCar(request,car):
    print(car)
    return json({'car':car})
