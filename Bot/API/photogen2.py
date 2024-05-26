from Bot.settings.setting import settings
import os
import requests
import json
n=0
photspath=os.path.join(os.path.dirname(__file__), "picture")
imagelink=f"{photspath}/{n}.png"




def text_to_image(text):
  URL=f"https://api.cloudflare.com/client/v4/accounts/{settings.CLOUDFLARE_ID}/ai/run/@cf/lykon/dreamshaper-8-lcm"
  headers = {
        "Authorization": f"Bearer {settings.CLOUDFLARE_API_KEY}",
        "Content-Type": "application/json"
    }
  
  promt={
    "prompt": text,
  }
  
  response = requests.post(URL, headers=headers, json=promt)
  try:
    with open(imagelink, "wb") as f:
      f.write(response.content)
  except Exception as e:
    print(e)
  finally:
    return  imagelink
  
  

  

  
