pip install pyqrcode pypng

import pyqrcode

data = "https://github.com/vikixx13"

qr = pyqrcode.create(data)

qr.png("githubID.png", scale= 5)