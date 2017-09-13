from sanic import Blueprint
from view import jinja
from sanic.response import json
from module.wtform import PosForm,LedForm
from module.mongo import PosData
from bson.json_util import dumps
posData = PosData()

main = Blueprint('main')


@main.route("/files", methods=['GET','POST'])
async def filesIndex(request):
    form = PosForm(request)
    if request.method == 'POST':
        car = form.car.data #car
        x_value = form.x_value.data #car_x軸
        y_value = form.y_value.data #car_y軸
        vector_value = form.vector_value.data #car_vector
        posData.update(car,x_value,y_value,vector_value)
        return json({"success":"GOGOGO"})

@main.route('/')
async def index(request):
    car1 = posData.getlastcar(1)
    car2 = posData.getlastcar(2)
    return json(dumps(car1))
