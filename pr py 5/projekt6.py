import qrcode
from PIL import Image
import os

def make_qr(str,save):
    qr=qrcode.QRCode(
        version=4,  
        error_correction=qrcode.constants.ERROR_CORRECT_M, 
        box_size=10, 
        border=2, 
    )
    qr.add_data(str)
    qr.make(fit=True)

    img=qr.make_image()
    img.save(save)

def make_logo_qr(str,logo,save):
    qr=qrcode.QRCode(
        version=4,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=8,
        border=2
    )

    qr.add_data(str)

    qr.make(fit=True)
    img=qr.make_image()

    img=img.convert("RGBA")

    if logo and os.path.exists(logo):
        icon=Image.open(logo)
        img_w,img_h=img.size

        factor=4
        size_w=int(img_w/factor)
        size_h=int(img_h/factor)

        icon_w,icon_h=icon.size
        if icon_w>size_w:
            icon_w=size_w
        if icon_h>size_h:
            icon_h=size_h
        icon=icon.resize((icon_w,icon_h),Image.ANTIALIAS)

        w=int((img_w-icon_w)/2)
        h=int((img_h-icon_h)/2)
        icon=icon.convert("RGBA")
        img.paste(icon,(w,h),icon)

    img.save(save)

if __name__=='__main__':
    save_path='theqrcode.png'
    logo='logo.jpg'

    str=input('Please input your string：')

    make_logo_qr(str,logo,save_path)
