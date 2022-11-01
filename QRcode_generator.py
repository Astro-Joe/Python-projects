import pyqrcode
from pyqrcode import QRCode

# String represents the QRcode.
link = "https://www.makeuseof.com/python-projects-for-beginners/"

# Generate QRCode
code = pyqrcode.create(link)

# Create and save the png file naming "myqr.png"
code.svg("firstQRcode.svg", scale = 8)
