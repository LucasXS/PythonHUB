# pip install pyqrcode
# pip install pypng

# read more: https://pypi.org/project/PyQRCode/

import pyqrcode
import png

qr = "https://python.org.br/"    # paste any url here
url = pyqrcode.create(qr)
# url.png('Desktop\\qr.png', scale=8)

print(url.terminal())

