import zipfile
import os
def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            if file == 'zipit.py':
                pass
            else:
                ziph.write(os.join(root,file))

if __name__=="main":
    zipf = zipfile.ZipFile('zip.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('.', zipf)
    zipf.close()
