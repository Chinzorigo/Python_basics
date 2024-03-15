import pyqrcode

text = input("Enter the text to generate QR code: ")

qr_code = pyqrcode.create(text)
qr_code.svg('qr_code.svg', scale=8)  # saving the QR code as svg file
print('QR code generated successfully')
