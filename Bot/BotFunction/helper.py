def devdeveloper_message(): return f"""

👉🏻For more information, please contact the developer.
👉🏻Developer: @thepr0fessor
Github:<a href="https://github.com/swadhinbiswas/AIBOT"> link</a> 


"""



def strat_maessage(name):
  
  return f"""<b><i>Hi! @{name}👋 </i>
                       I am The Professor The BOT</b>
<b><i>I can help you with the following things:</i> </b>
<b> 🖼 I can create images from text</b>.
<b> 🧾I can create text from images.</b>
<b> 🎉 I can create memes.</b>
<b> 📚I can translate text.</b>
<b> I can generate text from audio.🎙</b>
<b> I can generate audio from text.📒🎙</b>
<b> I can manupulate images.</b>
<b> I can generate text from text.</b>

<i>{devdeveloper_message()}</i>



"""




def help_message(name):
  return f"""<b><i>Hi! @{name}👋 </i>
<b>👉🏻Here are the commands you can use:</b>
<b>
cmd : /start[To start the bot]
cmd : /help[To get help]
cmd : /imagine [To convert text to image]
cmd : /img [To convert image to text]
cmd : /meme [To create meme]
cmd : /translate [To translate text]
cmd : /audio [To convert text to audio]
cmd : /audio[dalle] [To convert audio to text]
</b>
<i>{devdeveloper_message()}</i>


"""




def imagine_message(name):
   return f"""<b><i>Hi! @{name}👋 </i></b>
Please enter the text you want to convert to image.

<b>👉🏻Example:</b>

/imagine A beautiful day in the city.
or /imagine2 A beautiful day in the city.


<i>{devdeveloper_message()}</i>

"""

def imagine_message(name):
   return f"""<b><i>Hi! @{name}👋 </i></b>
Please enter the text you want to convert to image.

<b>👉🏻Example:</b>

/imagine A beautiful day in the city.
or /imagine2 A beautiful day in the city.


<i>{devdeveloper_message()}</i>

"""

def meme_message(name):
  return f"""<b><i>Hi! @{name}👋 </i>
Please enter the text you want to convert to meme.
<b>👉🏻Example:</b>

/meme A beautiful day in the city.

<i>{devdeveloper_message()}</i>


"""

def translate_message(name):return f"""<b><i>Hi! @{name}👋 </i>
if you want to translate text, please enter the text you want to translate.
<b>👉🏻Example:</b>


/translate A beautiful day in the city.

<i>{devdeveloper_message()}</i>

"""

def audio_message(name): return f"""<b><i>Hi! @{name}👋 </i>
Please enter the text you want to convert to audio.
<b>👉🏻Example:</b>

send me the audio file you want to convert to text.
than replay with  the command /audio to convert audio to text.


<i>{devdeveloper_message()}</i>

"""

def twitter_message(name): return f"""<b><i>Hi! @{name}👋 </i>
Please Provide Me a link of the twitter video you want to download.

<b>👉🏻Example:</b>

 cmd : /twitter <link of the twitter >



<i>{devdeveloper_message()}</i>

"""


