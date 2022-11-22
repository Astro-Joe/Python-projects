import pyqrcode
from pyqrcode import QRCode

# String represents the QRcode.
link = "https://www.youtube.com/watch?v=_uefYX5ACZ8"

# Generate QRCode
code = pyqrcode.create(link)

# Create and save the png file naming "myqr.png"
code.svg("secondQRcode.svg", scale = 8)
