from pyrogram import Client, filters
from Bot.settings.setting import settings


app = Client("thepr0fessor_bot", 
             api_id=settings.TELEGRAM_API_KEY,
             api_hash=settings.TELEGRAM_HASH, 
             bot_token=settings.TELEGRAM_BOT_TOKEN)

@app.on_message(filters.command("start"))
def start(app, message):
    
    name=message.from_user.username
    
    message.reply_text()








@app.on_message(filters.text)
def text_to_image(app, message):
    from Bot.API.photogen2 import text_to_image 
    imagelink=text_to_image(message.text)
    message.reply_photo(imagelink)
    
app.run()

