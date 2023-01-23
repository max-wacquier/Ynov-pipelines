import zipfile
from datetime import datetime

date = datetime.today().strftime('%Y-%m-%d')

with zipfile.ZipFile("release-" + date + ".zip", mode="w") as archive:
    archive.write("app.py")
    archive.write("tools.py")