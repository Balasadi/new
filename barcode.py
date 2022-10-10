#improting the module
import qrcode

#creating a variable for the text in which we want the QR code to link us
qr = qrcode.make('ProbeQ')

#saving the QR code as a png file
qr.save('images/probeq.png')