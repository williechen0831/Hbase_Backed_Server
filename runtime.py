from view.base import app
from view.debug import debug
from view.main import main
from view.api import api
from conf.dask_conf import client
import zipfile
import os
def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(file)

zipf = zipfile.ZipFile('module.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir('module', zipf)
zipf.close()
zipf = zipfile.ZipFile('conf.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir('conf', zipf)
zipf.close()
client.upload_file('module.zip')
client.upload_file('conf.zip')
app.blueprint(debug, url_prefix='/debug')
app.blueprint(api, url_prefix='/api')
app.blueprint(main)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8087)
