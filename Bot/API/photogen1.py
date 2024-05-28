from Bot.settings.setting import settings
# from ..settings.setting import settings
import os
import requests
import json
n=1
photspath=os.path.join(os.path.dirname(__file__), "picture")
image=f"{photspath}/{n}.png"




def text_to_stabilityimage(text):
  URL=f"https://api.cloudflare.com/client/v4/accounts/{settings.CLOUDFLARE_ID2}/ai/run/@cf/stabilityai/stable-diffusion-xl-base-1.0"
  headers = {
        "Authorization": f"Bearer {settings.CLOUDFLARE_API_KEY2}",
        "Content-Type": "application/json"
    }
  
  promt={
    "prompt": text,
  }
  
  response = requests.post(URL, headers=headers, json=promt)
  try:
    with open(image, "wb") as f:
      f.write(response.content)
  except Exception as e:
    print(e)
  finally:
    return  image
  
