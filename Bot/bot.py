from pyrogram import Client, filters
from Bot.settings.setting import settings
from Bot.API.photogen2 import text_to_image
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

 

  @app.on_message(filters.text)
  def text_to_text(app, message):
        result=texttotext(message.text)
        message.reply_text(result)
        
        

  @app.on_message(filters.command("imagine2"))
  def imagine2(app, message):
        name=message.from_user.username
        
        if message.text=="/imagine2":
          
            message.reply_text(f"""{name}This is the imagine2 command
                           <b>👉🏻Example:</b>
                           
                           """)
        else:
          message.reply_text("Please wait while I convert your image to text.")
          message.reply_text("This may take a while.")
          message.delete()
          # imagelink=text_to_image(message.text)
          message.reply_photo(f"""
                              <b>👉🏻This Stage is under Development</b>
                              
                              
                              """)
      
  
  

