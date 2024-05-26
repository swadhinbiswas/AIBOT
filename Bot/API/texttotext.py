import os
import requests
import json
from Bot.settings.setting import settings

def texttotext(text):
    response = requests.post(
      f"https://api.cloudflare.com/client/v4/accounts/{settings.CLOUDFLARE_ID}/ai/run/@hf/google/gemma-7b-it",
        headers={"Authorization": f"Bearer {settings.CLOUDFLARE_API_KEY}"},
        json={
          "messages": [
            {"role": "system", "content": "You are a friendly assistant"},
            {"role": "user", "content": text}
          ]
        }
    )
    result = response.json()
    return result['result']['response']


