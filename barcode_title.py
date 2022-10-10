import treepoem

img = treepoem.generate_barcode(
    barcode_type='qrcode',
    data='http://192.168.7.243:50070/',
    options={"eclevel": "Q"}
)
img.convert('1').save('qr.gif')