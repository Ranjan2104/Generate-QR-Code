# Developed by Amresh Ranjan.

import pyqrcode

link = 'Facebook.com'

QR = pyqrcode.create(link)

QR.png('Facebook.png', scale= 10)
