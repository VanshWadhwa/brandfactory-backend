
import pyqrcode
from PIL import Image,ImageTk

# text = "vansh Wadhwa"
text = "https://www.bloombergquint.com/markets/the-dogecoin-joke-is-turning-serious-in-latest-crypto-binge?utm_campaign=fullarticle&utm_medium=referral&utm_source=inshorts"

qr = pyqrcode.create(text)
filename = "qrcodetry.png"
# qr.svg(filename , scale = 10)
qr.png(filename , scale = 10)
# pip install pypng 
# for .png
print("DONE")

def createQRcode(text , filenameToBeSavedAs):
    qr = pyqrcode.create(text)
    qr.png(filenameToBeSavedAs , scale = 10)
    
url = pyqrcode.create("vansh")
url.png('uca-colors.png', scale= 25, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])