from sanic import Sanic
from sanic_jinja2 import SanicJinja2

app = Sanic(__name__)
jinja = SanicJinja2(app)

from view.debug import debug
from view.main import main
app.blueprint(debug, url_prefix='/debug')
app.blueprint(main)

app.config['WTF_CSRF_SECRET_KEY'] = 'top secret!'
session = {}

@app.middleware('request')
async def add_session(request):
    request['session'] = session


