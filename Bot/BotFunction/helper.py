def devdeveloper_message():
    return f"""
💻 <b>Developer:</b> <a href="https://github.com/swadhinbiswas">Swadhin Biswas</a>
🔗 <a href="https://github.com/swadhinbiswas/AIBOT">GitHub Repository</a>
"""

def strat_maessage(name):
    return f"""🎓 <b>Hi @{name}! I'm The Professor Bot</b> 🤖

🌟 <b>What I can do:</b>
🎨 Text → Image Generation
📖 Image → Text Reading
😂 Meme Creation
🌐 Text Translation
🎙️ Audio → Text / Text → Audio
📄 PDF Operations (Unlock/Convert)
🔐 File Encryption/Decryption
🔗 QR Code Generation
📡 Morse Code Conversion
📱 Social Media Downloads
🌍 Domain & IP Information
📸 Website Screenshots

{devdeveloper_message()}
"""

def help_message(name):
    return f"""📚 <b>Hi @{name}! Commands Menu</b> 🤖

🚀 <b>Quick Commands:</b>
• <code>/start</code> - Start the bot
• <code>/help</code> - Show this menu
• <code>/imagine</code> - Text → Image
• <code>/img</code> - Image → Text
• <code>/meme</code> - Create memes
• <code>/translate</code> - Translate text
• <code>/audio</code> - Audio conversion
• <code>/twitter</code> - Download videos
• <code>/qrcode</code> - Generate QR codes
• <code>/encrypt</code> - Encrypt text
• <code>/decrypt</code> - Decrypt text

{devdeveloper_message()}
"""

def imagine_message(name):
    return f"""🎨 <b>Hi @{name}! Image Generator</b> ✨

💡 <b>Enter text to create an image:</b>

<b>Examples:</b>
• <code>/imagine A beautiful sunset over mountains</code>
• <code>/imagine2 Futuristic city at night</code>

{devdeveloper_message()}
"""

def meme_message(name):
    return f"""😂 <b>Hi @{name}! Meme Creator</b> 🎭

🎨 <b>Enter your meme text:</b>

<b>Example:</b>
<code>/meme When you finally fix that bug</code>

{devdeveloper_message()}
"""

def translate_message(name):
    return f"""🌐 <b>Hi @{name}! Text Translator</b> 🔄

🗣️ <b>Enter text to translate:</b>

<b>Example:</b>
<code>/translate Hello, how are you today?</code>

{devdeveloper_message()}
"""

def audio_message(name):
    return f"""🎙️ <b>Hi @{name}! Audio Converter</b> 🔊

🎵 <b>Send me an audio file</b>
Then reply with <code>/audio</code> to convert to text

{devdeveloper_message()}
"""

def twitter_message(name):
    return f"""📱 <b>Hi @{name}! Video Downloader</b> ⬇️

🔗 <b>Send me a Twitter video link:</b>

<b>Example:</b>
<code>/twitter https://twitter.com/user/status/123456</code>

{devdeveloper_message()}
"""
