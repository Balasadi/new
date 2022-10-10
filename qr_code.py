#importing the module
import qrcode

# creating the variable for the QR code
qr = qrcode.QRCode(
    version = 1,
    box_size = 35,
    border = 10
    )

# adding a link for the QR code to open
data = 'https://www.ibomma.org/telugu-movies/'
qr.add_data(data)
qr.make(fit=True)

# adding the color
img = qr.make_image(fill = 'black', back_color = 'white')
img.save('images/ibomma.png')