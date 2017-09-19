from view.base import app
from view.debug import debug
from view.main import main
from view.api import api
from conf.dask_conf import client
import subprocess
app.blueprint(debug, url_prefix='/debug')
app.blueprint(api, url_prefix='/api')
app.blueprint(main)
subprocess.call('python3 ./module/zipit.py')
copyfile('./module/zipit.py', './conf/zipit.py')
subprocess.call('python3 ./conf/zipit.py')
subprocess.call('rm ./conf/zipit.py')
subprocess.call('mv ./conf/zip.zip conf.zip')
subprocess.call('rm ./module/zip.zip module.zip')
client.upload_file('module.zip')
client.upload_file('conf.zip')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8087)
