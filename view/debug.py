from sanic import Blueprint
from view import jinja
from module.wtform import PosForm,LedForm
debug = Blueprint('debug')

@debug.route("/", methods=['GET','POST'])
async def debugIndex(request):
    form = PosForm(request)
    if request.method == 'POST':
        time = form.time.data #time
        car = form.car.data #car
        car_collect_x = car + ":" + "x"
        car_collect_y = car + ":" + "y"
        car_collect_vector = car + ":" + "vector"
        x_value = form.x_value.data #car_x軸
        y_value = form.y_value.data #car_y軸
        vector_value = form.vector_value.data #car_vector
        return json({"success":"GOGOGO"})
    else:
        return jinja.render('index.html', request)

@debug.route("/led",methods=['GET','POST'])
async def web_led(request):
    form = LedForm(request)
    if request.method == 'POST':
        time = form.time.data
        main = form.main.data
        nums = form.nums.data
        first = form.first.data
        second = form.second.data
        third = form.third.data
        fourth = form.fourth.data
        fifth = form.fifth.data
        sixth =form.sixth.data
        CARfirst="CAR1:1st"
        CARsecond="CAR1:2nd"
        CARthird="CAR1:3rd"
        CARfourth="CAR1:4th"
        CARfifth="CAR1:5th"
        CARsixth="CAR1:6th"
        CARmain="CAR1:main"
        CARnums="CAR1:nums"

        return json({"success":"GOGOGO"})
    else:
        return jinja.render('index2.html', request)
