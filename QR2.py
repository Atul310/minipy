#This is advance qr code generator 
import qrcode as qr
from PIL import Image

my_qr = qr.QRCode(version=1,
                  error_correction=qr.constants.ERROR_CORRECT_H,
                  box_size=20,
                  border=2
                  )
my_qr.add_data("https://schoolworkspro.com/")
my_qr.make(fit=True)
img = my_qr.make_image(fill_color="black",back_color="red")

 
img.save("save.png")