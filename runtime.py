from view.base import app
from view.debug import debug
from view.main import main
from view.api import api
from conf.dask_conf import client
import subprocess
app.blueprint(debug, url_prefix='/debug')
app.blueprint(api, url_prefix='/api')
app.blueprint(main)
client.upload_file('shared.py') 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8087)
