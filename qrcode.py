# First install pyqrcode library using command line ya linux terminal

import pyqrcode # Then allow library access

# make variable to store link below there
link = "www.facebook.com" 

# make variable to create QR_CODE like this
url=pyqrcode.create(link)

# Then save it in any director Or folder
img=url.png('QRCode.png',scale=6)
