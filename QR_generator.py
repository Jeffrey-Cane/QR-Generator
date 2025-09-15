#pip install PyQRCode
#pip install pypng
import pyqrcode
import png
link = "Enter your LinkedIn profile link here"
qr_code = pyqrcode.create(link)
qr_code.png('linkedin_qr_code.png', scale=6)
# This code generates a QR code for the specified link and saves it as 'linkedin_qr_code.png'.
# The scale parameter controls the size of the QR code image.