import qrcode
from PIL import Image
import json 
import os
import requests

jsonfile=os.path.join(os.path.dirname(__file__), "qrcodeicon.json")
with open(jsonfile, "r") as f:
    data=json.load(f)
    
iconfolder=os.path.join(os.path.dirname(__file__), "icon")

def createqr(url:str):
   x=url.split('.')
   x=x[1]
   with open (f"{iconfolder}/icon.png", "wb") as f:
      if data[x]=="":
         icon=requests.get("https://cdn.icon-icons.com/icons2/2699/PNG/512/python_logo_icon_168886.png",stream=True)
      else:
         reponce=requests.get(data[x],stream=True)
         
      for chunk in reponce.iter_content(chunk_size=128):
             f.write(chunk)
             
   icon=Image.open(f"{iconfolder}/icon.png")
   basewidth=100
   wpercent=(basewidth/float(icon.size[0]))
   hsize=int((float(icon.size[1])*float(wpercent)))
   Qrcode=qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
   )
   Qrcode.add_data(url)
   Qrcode.make()
   Qrcodeimg=Qrcode.make_image(fill_color="white", back_color="black",hsize=hsize).convert("RGB")
#    icon=icon.resize((basewidth,hsize), Image.ANTIALIAS)
   postion=((Qrcodeimg.size[0]-icon.size[0])//2,(Qrcodeimg.size[1]-icon.size[1])//2)
   Qrcodeimg.paste(icon, postion)
   Qrcodeimg.save(f"{iconfolder}/qrcode.png")
   return f"{iconfolder}/qrcode.png"











