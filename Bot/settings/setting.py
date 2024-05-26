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



settings = Settings()



  
  