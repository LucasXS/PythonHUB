# pip install pyqrcode
# read more: https://pypi.org/project/PyQRCode/

import pyqrcode

qr = "https://python.org.br/"    # paste any url here
url = pyqrcode.create(qr)

print(url.terminal())

