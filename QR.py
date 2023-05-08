#This is simple QR code 
import qrcode as qr # qr is alias name {alternative name}
mycode = qr.make("https://www.youtube.com/watch?v=WmbU3WBaoR0&list=PLKnIA16_RmvbAlyx4_rdtR66B7EHX5k3z&index=10")
mycode.save("campusxyoutbelink.png")

