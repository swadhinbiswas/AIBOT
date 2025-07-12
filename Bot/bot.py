from pyrogram import Client, filters
# from pyrogram.types import MenuButtonCommands
from Bot.settings.setting import settings
from Bot.BotFunction.urlshortner import UrlShortner
from Bot.API.photogen2 import text_to_image
from Bot.API.photogen1 import text_to_stabilityimage
from Bot.API.texttotext import texttotext
from Bot.BotFunction.twitterdounloader import twitter_download
from Bot.BotFunction.helper import help_message, strat_maessage, imagine_message,twitter_message
# from Bot.API.Geminiapp import Geminiapp
import os
from Bot.BotFunction.urlshortner import UrlShortner
from Bot.BotFunction.morsecode import txttomorsecode
from Bot.BotFunction.qrcodehelper import createqr
from Bot.API.encrypttext import encrypt_text,decrypt_text,encrypt_image,decrypt_image
from Bot.API.iptress import trackip
from Bot.API.htmltopdf import html_to_pdf
from Bot.API.domaininfo import domaininfo
from Bot.API  import AIImageAPI
from Bot.API import url_to_image
import os


class Bot:

  app = Client("thepr0fessor_bot",
              api_id=settings.TELEGRAM_API_KEY,
              api_hash=settings.TELEGRAM_HASH,
              bot_token=settings.TELEGRAM_BOT_TOKEN)



#   app.set_chat_menu_button("menu", MenuButtonCommands())

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
          imagelink=AIImageAPI().generate_image(message.text)
          if not imagelink:
              message.reply_text("❌ Error generating image. Please try again.")
              return
          message.reply_text("Image generated successfully!")
          # Send the image
          if isinstance(imagelink, list):
              for link in imagelink:
                  message.reply_photo(link)
          else:
              # If a single image link is returned
              if imagelink.startswith("http"):  # Check if it's a URL
                  message.reply_photo(imagelink)
              else:
                  message.reply_photo("Image generated successfully!", photo=imagelink)

  @app.on_message(filters.command("meme"))
  def meme(app, message):
        name=message.from_user.username

        if message.text=="/meme":
          message.reply_text(f"""{name}This is the meme command
                            <b>👉🏻This Stage is under Development</b>

                           """)

        else:
            message.reply_text(f"""{name}This is the meme command
                            <b>👉🏻This Stage is under Development</b>

                           """)
  @app.on_message(filters.command("translate"))
  def translate(app, message):
        name=message.from_user.username

        if message.text=="/translate":
              message.reply_text(f"""{name}This is the translate command
                              <b>👉🏻This Stage is under Development</b>

                                 """)

        else:
                  message.reply_text(f"""{name}This is the translate command
                                 <b>👉🏻This Stage is under Development</b>

                           """)

  @app.on_message(filters.command("audio"))
  def audio(app, message):
        name=message.from_user.username

        if message.text=="/audio":
                  message.reply_text(f"""{name}This is the audio command
                                    <b>👉🏻This Stage is under Development</b>

                                     """)

        else:
             message.reply_text(f"""{name}This is the audio command
                            <b>👉🏻This Stage is under Development</b>

                           """)


  @app.on_message(filters.command("video"))
  def video(app, message):

        name=message.from_user.username

        if message.text=="/video":
              message.reply_text(f"""{name}This is the video command
                              <b>👉🏻This Stage is under Development</b>

                                 """)

        else:

            message.reply_text(f"""{name}This is the video command
                            <b>👉🏻This Stage is under Development</b>

                           """)

  @app.on_message(filters.command("image"))
  def image(app, message):

        if message.text=="/image":
          x=imagine_message(message.from_user.username)
          message.reply_text(x)

        else:
            name=message.from_user.username
            message.reply_text(f"""{name}This is the image command
                              <b>👉🏻This Stage is under Development</b>

                              """)

  @app.on_message(filters.command("speedtest"))
  def speedtest(app, message):
        name=message.from_user.username
        if message.text=="/speedtest":

          message.reply_text(f"""{name}This is the speedtest command
                            <b>👉🏻This Stage is under Development</b>

                           """)

        else:

            message.reply_text(f"""{name}This is the speedtest command
                              <b>👉🏻This Stage is under Development</b>

                              """)



  @app.on_message(filters.all & filters.command("see"))
  async def photo_handler(client, message):

         if message.text=="/see":
            await message.reply_text("Please provide the photo's file ID after the command")

         else:
            user_images={}
            # Store the photo's file ID with the user's ID as key
            user_images[message.from_user.id] = message.photo.file_id
            await message.reply_text("Photo received. Now, send /see to get the photo's file ID.")
            await message.reply_text("Please wait while I am downloading the image")
            await message.reply_text(user_images[message.from_user.id])


  @app.on_message(filters.command("qrcode"))
  async def qrcode(app, message):
        if message.text=="/qrcode":
          await message.reply_text("Please provide the url after the command")
        else:
             url=message.text.split(" ")[1]
             img=createqr(url)
             await message.reply_photo(img)

             os.remove(img)






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
  async def urlshortner(app, message):
        name=message.from_user.username

        if message.text=="/urlshortner":
          await message.reply_text(f"""{name}Please provide the url after the command""")
        else:
            await message.reply_text(f"""{name}Hold On a second""")

            x=UrlShortner().shorten(message.text.split(" ")[1])
            await message.reply_text(x)


  @app.on_message(filters.video & filters.command("gif"))
  def gif(app, message):
        name=message.from_user.username
        message.reply_text(f"""{name}This is the gif command
                            <b>👉🏻This Stage is under Development</b>

                           """)


  @app.on_message(filters.command("morsecode"))
  async def morsecode(app, message):
        name=message.from_user.username

        if message.text=="/morsecode":
              await message.reply_text(f"""{name}Please provide the text after the command""")

        else:
            await message.reply_text(f"""{name}Hold On a second""")

            text=message.text.split(" ")[1]
            result=txttomorsecode(text)
            await message.reply_text(result)



  @app.on_message(filters.command("encrypt"))
  async def encrypt(app, message):
            name=message.from_user.username

            if message.text=="/encrypt":
              await message.reply_text(f"""{name}Please provide the text after the command""")

            else:
                  await message.reply_text(f"""{name}Hold On a second""")
                  text=message.text.split(" ")[1]
                  result=encrypt_text(text)
                  await message.reply_text(result)

  @app.on_message(filters.command("decrypt"))
  async def decrypt(app, message):
            name=message.from_user.username

            if message.text=="/decrypt":
              await message.reply_text(f"""{name}Please provide the text after the command""")

            else:
                  await message.reply_text(f"""{name}Hold On a second""")
                  text=message.text.split(" ")[1]
                  result=decrypt_text(text)
                  await message.reply_text(result)

  @app.on_message(filters.command("iptack"))
  async def iptack(app, message):
            name=message.from_user.username

            if message.text=="/iptack":
              await message.reply_text(f"""{name}Please provide the ip after the command""")

            else:
                  await message.reply_text(f"""{name}Hold On a second""")
                  ip=message.text.split(" ")[1]
                  result=trackip(ip)
                  await message.reply_text(result)


  @app.on_message(filters.command("webtopdf"))
  async def webtopdf(app, message):
            name=message.from_user.username

            if message.text=="/webtopdf":
              await message.reply_text(f"""{name}Please provide the url after the command""")

            else:
                  await message.reply_text(f"""{name}Hold On a second""")
                  url=message.text.split(" ")[1]
                  result=html_to_pdf(url)
                  await message.reply_document(result)


  # @app.on_message(filters.command("encrypt_image"))
  # async def encrypt_image(app, message):
  #           name=message.from_user.username

  #           if message.text=="/encrypt_image":
  #             await message.reply_text(f"""{name}Please provide the image file after the command""")

  #           else:
  #                 await message.reply_text(f"""{name}Hold On a second""")
  #                 image=message.text.split(" ")[1]
  #                 result=encrypt_image(image)
  #                 await message.reply_photo(result)
  @app.on_message(filters.command("dominlookup"))
  async def dominlookup(app, message):

    if message.text=="/dominlookup":
      await message.reply_text("Please provide the domain name after the command with out https://www.")

    else:
      await message.reply_text("Please wait while I am fetching the domain information")
      domain=message.text.split(" ")[1]
      result=domaininfo(domain)
      await message.reply_text(result,parse_mode="MarkdownV2")
  @app.bot.on_message(filters.command("urltoimage"))
  async def urltoimage(app, message):
        if message.text=="/urltoimage":
            await message.reply_text("Please provide the URL after the command")
        else:
            url = message.text.split(" ")[1]
            await message.reply_text("Please wait while I am converting the URL to image")
            result = url_to_image(url)
            if isinstance(result, str) and result.startswith("Error:"):
                await message.reply_text(result)
            else:
                await message.reply_photo(result, caption="Here is the image from the URL")


  @app.on_message(filters.text & ~filters.command(["start", "help", "imagine","img","twitter","urlshortner","qrcode","morsecode","encrypt","decrypt","text_to_text","decrypt_image","encrypt_image","gemini","geminiapp","iptack","webtopdf","dominlookup","speedtest","see","gif","translate","audio","video","image","meme"]))
  def text_to_text(app, message):
        result=texttotext(message.text)
        message.reply_text(result)
