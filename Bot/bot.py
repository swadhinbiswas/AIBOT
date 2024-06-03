from pyrogram import Client, filters
from Bot.settings.setting import settings
from Bot.BotFunction.urlshortner import UrlShortner
from Bot.API.photogen2 import text_to_image
from Bot.API.photogen1 import text_to_stabilityimage
from Bot.API.texttotext import texttotext
from Bot.BotFunction.twitterdounloader import twitter_download
from Bot.BotFunction.helper import help_message, strat_maessage, imagine_message,twitter_message
from Bot.API.Geminiapp import Geminiapp
import os



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
     
               
  
  @app.on_message(filters.all & filters.command("see"))
  async def photo_handler(client, message):
    user_images={}
    # Store the photo's file ID with the user's ID as key
    user_images[message.from_user.id] = message.photo.file_id
    await message.reply_text("Photo received. Now, send /see to get the photo's file ID.")
    await message.reply_text("Please wait while I am downloading the image")
    await message.reply_text(user_images[message.from_user.id])
    
    
  @app.on_message(filters.command("twitter"))
  async def twitter(app, message):
            name=message.from_user.username
            if message.text=="/twitter":
              x=twitter_message(name)
              message.reply_text(x)
            else:
              url=message.text.split(" ")[1]
              await message.reply_text("Please wait while I download the video.")
              await message.reply_text("This may take a while.")
              
              filename= twitter_download(url)
              await message.reply_video(filename)
              if os.path.exists(filename):
                os.remove(filename)
                
  @app.on_message(filters.command("urlshortner"))
  def urlshortner(app, message):
        name=message.from_user.username
        message.reply_text(f"""{name}This is the urlshortner command
                            <b>👉🏻This Stage is under Development</b>
                           
                           """)
              

  @app.on_message(filters.text) 
  def text_to_text(app, message):
        result=texttotext(message.text)
        message.reply_text(result)
  


