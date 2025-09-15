#pip install pyzbar
#pip install pillow
from pyzbar.pyzbar import decode
from PIL import Image   
# Open the image file
image = Image.open('linkein_qr_code.png')# enter the qr image here
# Decode the QR code
decoded_objects = decode(image) 
# Print the decoded data
print(decoded_objects[0].data.decode('utf-8')) if decoded_objects else print("No QR code found.")
