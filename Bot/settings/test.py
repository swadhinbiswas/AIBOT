from dotenv import load_dotenv
import os
load_dotenv()


sefty_settings = os.getenv('SEFT_API_KEY')

print(sefty_settings)