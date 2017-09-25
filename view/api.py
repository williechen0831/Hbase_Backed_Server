"""for api Blueprint module"""
from sanic import Blueprint
from sanic.response import json
from module.mongo import PosData
from module.compute import block_check, getrecentcar_parallel

posData = PosData()
api = Blueprint('api')

@api.route('/car/<car>')
async def findCar(request, car):
    """function for find one car"""
    try:
        dbCar = posData.getlastcar(int(car))[0]
    except TypeError:
        return json({'msg':'err'})
    return json({
        'car': dbCar.get('car'),
        'X': dbCar.get('X'),
        'Y': dbCar.get('Y'),
        'V': dbCar.get('V'),
        'time': dbCar.get('time')})


@api.route('/led')
async def getLed(request):
    """api route for find six car"""
    Car = block_check(getrecentcar_parallel())
    return json(Car)
