# pip install pyqrcode
# pip install pypng

# import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode


# String which represents thr QR code
s = "www.example.org"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the svg file naming "example.svg"
url.svg("example.svg", scale = 8)

# Create and save the png file naming "example.png"
url.png("example.png", scale = 6)
