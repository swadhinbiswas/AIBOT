from pyrogram import Client, filters
from Bot.settings.setting import settings
from Bot.API.photogen2 import text_to_image
from Bot.API.photogen1 import text_to_stabilityimage
from Bot.API.texttotext import texttotext
from Bot.BotFunction.helper import help_message, strat_maessage, imagine_message



class Bot:

  app = Client("thepr0fessor_bot", 
              api_id=settings.TELEGRAM_API_KEY,
              api_hash=settings.TELEGRAM_HASH, 
              bot_token=settings.TELEGRAM_BOT_TOKEN)



  @app.on_message(filters.command("start"))
  def start(app, message):
        
        name=message.from_user.username
        if message.text=="/start":
          x=strat_maessage(name)
        message.reply_text(x)
        
  @app.on_message(filters.command("help"))
  def help(app, message):
        
        name=message.from_user.username
        x=help_message(name)
        message.reply_text(x)



  @app.on_message(filters.command("img"))
  def img(app, message):
        
        if message.text=="/img":
          x=imagine_message(message.from_user.username)
          message.reply_text(x)
        else:
          message.reply_text("Please wait while I convert your text to image.")
          message.reply_text("This may take a while.")
          img=text_to_stabilityimage(message.text)
          message.reply_photo(img)
          #make both in One function
  

  @app.on_message(filters.command("imagine"))
  def imagine(app, message):
    
    
        if message.text=="/imagine":
          x=imagine_message(message.from_user.username)
          message.reply_text(x)
        else:
          message.reply_text("Please wait while I convert your text to image.")
          message.reply_text("This may take a while.")
          imagelink=text_to_image(message.text)
          message.reply_photo(imagelink)


  @app.on_message(filters.command("meme"))
  def meme(app, message):
        name=message.from_user.username
        message.reply_text(f"""{name}This is the meme command
                            <b>👉🏻This Stage is under Development</b>
                           
                           """)
  @app.on_message(filters.command("translate"))
  def translate(app, message):
        name=message.from_user.username
        message.reply_text(f"""{name}This is the translate command
                            <b>👉🏻This Stage is under Development</b>
                           
                           """)
        
  @app.on_message(filters.command("audio"))
  def audio(app, message):
        name=message.from_user.username
        message.reply_text(f"""{name}This is the audio command
                            <b>👉🏻This Stage is under Development</b>
                           
                           """)
        
        
  @app.on_message(filters.command("video"))
  def video(app, message):
        name=message.from_user.username
        message.reply_text(f"""{name}This is the video command
                            <b>👉🏻This Stage is under Development</b>
                           
                           """)
        
  @app.on_message(filters.command("image"))
  def image(app, message):
        name=message.from_user.username
        message.reply_text(f"""{name}This is the image command
                            <b>👉🏻This Stage is under Development</b>
                           
                           """)
        
  @app.on_message(filters.command("speedtest"))
  def speedtest(app, message):
        name=message.from_user.username
        message.reply_text(f"""{name}This is the speedtest command
                            <b>👉🏻This Stage is under Development</b>
                           
                           """)
        
        
  @app.on_message(filters.text)
  def text_to_text(app, message):
        result=texttotext(message.text)
        message.reply_text(result)
  


