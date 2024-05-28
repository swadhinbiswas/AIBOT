from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
  CLOUDFLARE_API_KEY=os.getenv('CLOUDFLARE_API_KEY')
  TELEGRAM_BOT_TOKEN=os.getenv('TELEGRAM_BOT_TOKEN')
  CLOUDFLARE_ID=os.getenv('CLOUDFLARE_ID')
  URL=f"https://api.cloudflare.com/client/v4/accounts/{CLOUDFLARE_ID}/ai/run/@hf/google/gemma-7b-it"
  TELEGRAM_API_KEY = os.getenv('TELEGRAM_API_KEY')
  TELEGRAM_HASH=os.getenv('TELEGRAM_HASH')
  CLOUDFLARE_ID2=os.getenv('CLOUDFLARE_ID2')
  CLOUDFLARE_API_KEY2=os.getenv('CLOUDFLARE_API_KEY2')
  SEFTY_SETTINGS=[
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]



settings = Settings()



  
  