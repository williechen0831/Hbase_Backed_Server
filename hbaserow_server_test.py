
from sanic import Sanic, response
import happybase
from sanic.response import json
from sanic_jinja2 import SanicJinja2

app = Sanic(__name__)
jinja = SanicJinja2(app)

# either WTF_CSRF_SECRET_KEY or SECRET_KEY should be set
app.config['WTF_CSRF_SECRET_KEY'] = 'top secret!'

#-------sanic wtf-------#



session = {}
@app.middleware('request')
async def add_session(request):
	request['session'] = session

from sanic_wtf import SanicForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(SanicForm):
	time = StringField('time', validators=[DataRequired()])
	car = StringField('car', validators=[DataRequired()])
	x_value = StringField('x_value', validators=[DataRequired()])
	y_value = StringField('y_value', validators=[DataRequired()])
	vector_value = StringField('vector_value', validators=[DataRequired()])
	submit = SubmitField('Get in')
#--------sanic wtf end --------#
class LoginForm2(SanicForm):
	time = StringField('time', validators=[DataRequired()])
	main = StringField('main', validators=[DataRequired()])
	nums = StringField('nums', validators=[DataRequired()])
	first = StringField('first', validators=[DataRequired()])
	second = StringField('second', validators=[DataRequired()])
	third = StringField('third', validators=[DataRequired()])
	fourth =StringField('fourth', validators=[DataRequired()])
	fifth =StringField('fifth', validators=[DataRequired()])
	sixth =StringField('sixth', validators=[DataRequired()])
	submit = SubmitField('Get in')

@app.route("/")
async def index(request):
	conn = happybase.Connection('10.0.56.26')
	table = conn.table('LED_DATA')
	dicthbase = {}
	jsondict = {}
	for key, data in table.scan():
		dicthbase["data"] = data
	print(dicthbase["data"])
	for key in dicthbase["data"]:
		jsondict[key.decode("utf-8")] = dicthbase["data"][key].decode("utf-8")
	print('-----------------------')
	print(jsondict)
	return json(jsondict)


@app.route("/web")
async def web(request):
	return jinja.render('index.html', request)


@app.route("/happybase_insert")
async def happybase_insert(request):
	connection = happybase.Connection('10.0.56.26')
	connection.open()
	print (connection.tables())

	table = connection.table('test2')
	table.put(b'row1', {b'family:cf1': b'123'})

	return json({"success":"true"})

@app.route("/files", methods=['GET', 'POST'])
async def post_json(request):
	form = LoginForm(request)
	print(form.name.data)
	if request.method == 'POST':
		time = form.time.data #time
		car = form.car.data #car
		car_collect_x = car + ":" + "x"
		car_collect_y = car + ":" + "y"
		car_collect_vector = car + ":" + "vector"		
		x_value = form.x_value.data #car_x軸
		y_value = form.y_value.data #car_y軸
		vector_value = form.vector_value.data #car_vector
		# check user password, log in user, etc.
		connection = happybase.Connection('10.0.56.26')
		connection.open()
		print (connection.tables())
		table = connection.table('bigdata')
		#table.put(b'row1', {b'family:cf1': b'123'})
		table.put(time,{car_collect_x:x_value})
		table.put(time,{car_collect_y:y_value})
		table.put(time,{car_collect_vector:vector_value})	

	
	
		return json({"success":"GOGOGO"})
		# here, render_template is a function that render template with context
	return json({"failed":"true"})
    
@app.route("/web_led")
async def web_led(request):
	return jinja.render('index2.html', request)

@app.route("/ledtest",methods=['GET', 'POST'])
async def post_json(request):
	form = LoginForm2(request)
	#print(form.name.data)
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

		connection = happybase.Connection('10.0.56.26')
		connection.open()
		print (connection.tables())
		table = connection.table('LED_DATA')

		table.put(time,{CARmain:main})
		table.put(time,{CARnums:nums})
		table.put(time,{CARfirst:first})
		table.put(time,{CARsecond:second})
		table.put(time,{CARthird:third})
		table.put(time,{CARfourth:fourth})
		table.put(time,{CARfifth:fifth})
		table.put(time,{CARsixth:sixth})
		
		return json({"success":"GOGOGO"})
		# here, render_template is a function that render template with context
		return json({"failed":"true"})


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8087)
