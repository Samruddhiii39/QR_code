import qrcode 
INP=input("Enter URL = ") 
qr= qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=20,border=10,)
qr.add_data(INP)
qr.make(fit=True)
img=qr.make_image(fill_color="PURPLE",back_color="WHITE")
img.save("YourQR.png")
