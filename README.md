# 🤖 AIBOT [BETA]

**The Professor Bot** - An advanced, versatile AI-powered Telegram bot built with Pyrogram

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://python.org)
[![Pyrogram](https://img.shields.io/badge/Pyrogram-Latest-green.svg)](https://docs.pyrogram.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🌟 Features Overview

### 🎨 **Creative & AI Tools**

- **🖼️ AI Image Generation** - Convert text descriptions into stunning images using AI
- **💬 AI Chatbot** - Powered by Google Gemma via Cloudflare AI
- **😂 Meme Creation** - Create custom memes _(In Development)_

### 🔧 **Utility Tools**

- **🔗 QR Code Generator** - Generate QR codes for any URL with custom icons
- **📏 URL Shortener** - Shorten long URLs for easy sharing
- **🔐 Text Encryption/Decryption** - Secure your text with encryption
- **📡 Morse Code Converter** - Convert text to/from Morse code
- **🌍 IP Tracker** - Get detailed information about IP addresses
- **🔍 Domain Lookup** - Comprehensive domain information and analysis

### 📱 **Media & Downloads**

- **🐦 Twitter Video Downloader** - Download videos from Twitter/X
- **📄 Website to PDF** - Convert any webpage to PDF
- **📸 URL to Image** - Generate screenshots of websites

### 🔧 **Development Features**

- **🔒 Secure Configuration** - Environment-based settings with .env support
- **📝 Comprehensive Logging** - Detailed logging for debugging
- **🐳 Docker Support** - Easy deployment with Docker
- **🎯 Modular Architecture** - Clean, maintainable code structure

## 📋 Implementation Status

### ✅ **Fully Implemented**

#### **AI & Creative**

- ✅ **AI Image Generation** - Text to image using Pollinations AI
- ✅ **AI Chatbot** - Google Gemma 7B via Cloudflare AI
- ✅ **Text Analysis** - Smart text processing and responses

#### **Utility Tools**

- ✅ **QR Code Generator** - Custom QR codes with domain-specific icons
- ✅ **URL Shortener** - Link shortening service
- ✅ **Text Encryption/Decryption** - Secure text encryption
- ✅ **Morse Code Converter** - Text ↔ Morse code conversion
- ✅ **IP Tracker** - Detailed IP geolocation and information
- ✅ **Domain Lookup** - WHOIS and domain analysis

#### **Media & Downloads**

- ✅ **Twitter Video Downloader** - Download Twitter/X videos
- ✅ **Website to PDF** - Convert webpages to PDF
- ✅ **URL to Screenshot** - Generate website screenshots

#### **Core Features**

- ✅ **Telegram Integration** - Full Pyrogram bot implementation
- ✅ **Error Handling** - Comprehensive error management
- ✅ **Logging System** - Detailed logging for debugging
- ✅ **Docker Support** - Containerized deployment

### 🚧 **In Development**

- 🚧 **Meme Generation** - Custom meme creation
- 🚧 **Text Translation** - Multi-language translation
- 🚧 **Audio Processing** - Text ↔ Audio conversion
- 🚧 **Video to GIF** - Video format conversion
- 🚧 **Speed Test** - Internet speed testing
- 🚧 **Instagram Downloader** - Instagram media downloads

### 📋 **Planned Features**

- 📋 **PDF Operations** - Unlock, merge, convert PDF files
- 📋 **File Encryption** - Encrypt/decrypt files
- 📋 **Face Search** - Facial recognition capabilities
- 📋 **OCR (Image to Text)** - Extract text from images
- 📋 **Email Search** - Find emails across the internet
- 📋 **Torrent Tracker** - Track torrent downloads

## 🎯 Available Commands

### **Basic Commands**

```bash
/start          - Start the bot and see welcome message
/help           - Display all available commands
```

### **AI & Creative**

```bash
/imagine <text>     - Generate AI image from text description
/img <text>         - Alternative image generation command
```

### **Utility Tools**

```bash
/qrcode <url>       - Generate QR code for URL
/urlshortner <url>  - Shorten long URLs
/encrypt <text>     - Encrypt text securely
/decrypt <text>     - Decrypt encrypted text
/morsecode <text>   - Convert text to Morse code
/iptack <ip>        - Track and analyze IP address
/dominlookup <domain> - Get domain information
/webtopdf <url>     - Convert webpage to PDF
/urltoimage <url>   - Generate website screenshot
```

### **Media & Downloads**

```bash
/twitter <url>      - Download Twitter/X videos
```

### **Development Commands**

```bash
/see               - Get photo file ID (for developers)
```

_Note: Any text message not starting with / will be processed by the AI chatbot._

## 🚀 Quick Start

### **Prerequisites**

- Python 3.8 or higher
- Telegram Bot Token (from [@BotFather](https://t.me/botfather))
- API Keys for various services (see Configuration section)

### **Installation**

1. **Clone the repository:**

   ```bash
   git clone https://github.com/swadhinbiswas/AIBOT.git
   cd AIBOT
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   Create a `.env` file in the root directory with the following:

   ```env
   # Required - Telegram Bot Configuration
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   TELEGRAM_API_KEY=your_api_id_here
   TELEGRAM_HASH=your_api_hash_here

   # Required - AI Features
   CLOUDFLARE_API_KEY=your_cloudflare_api_key
   CLOUDFLARE_ID=your_cloudflare_account_id
   GEMINI_API_KEY=your_gemini_api_key

   # Optional - Additional Features
   SCREENSHOT_API_KEY=your_screenshot_api_key
   HTMLTOPDF_API_KEY=your_pdf_api_key
   HOSTIO=your_hostio_api_key
   ```

4. **Run the bot:**
   ```bash
   python main.py
   ```

### **Docker Deployment**

1. **Build the Docker image:**

   ```bash
   docker build -t aibot .
   ```

2. **Run with environment file:**
   ```bash
   docker run -d --env-file .env --name aibot-container aibot
   ```

## 🔧 Configuration

### **Required API Keys**

| Service           | Purpose                       | Required | How to Get                                          |
| ----------------- | ----------------------------- | -------- | --------------------------------------------------- |
| **Telegram Bot**  | Core bot functionality        | ✅ Yes   | [@BotFather](https://t.me/botfather)                |
| **Telegram API**  | Pyrogram client               | ✅ Yes   | [my.telegram.org](https://my.telegram.org)          |
| **Cloudflare AI** | AI chatbot & image generation | ✅ Yes   | [Cloudflare Dashboard](https://dash.cloudflare.com) |

### **Optional API Keys**

| Service            | Purpose              | Required    | How to Get                                      |
| ------------------ | -------------------- | ----------- | ----------------------------------------------- |
| **Google Gemini**  | Enhanced AI features | ⚠️ Optional | [Google AI Studio](https://aistudio.google.com) |
| **Screenshot API** | Website screenshots  | ⚠️ Optional | Various providers                               |
| **HTML to PDF**    | PDF conversion       | ⚠️ Optional | Various providers                               |
| **HostIO**         | Domain lookup        | ⚠️ Optional | [Host.io](https://host.io)                      |

### **Project Structure**

```
AIBOT/
├── Bot/
│   ├── API/                  # External API integrations
│   │   ├── aiimage.py       # AI image generation
│   │   ├── texttotext.py    # AI chatbot
│   │   ├── encrypttext.py   # Text encryption
│   │   └── ...
│   ├── BotFunction/         # Bot utilities
│   │   ├── helper.py        # Message templates
│   │   ├── morsecode.py     # Morse code converter
│   │   ├── qrcodehelper.py  # QR code generation
│   │   └── ...
│   ├── settings/            # Configuration
│   └── bot.py              # Main bot logic
├── main.py                 # Entry point
├── requirements.txt        # Python dependencies
├── Dockerfile             # Docker configuration
└── README.md              # This file
```

## 📖 Usage Examples

### **AI Image Generation**

```
/imagine A beautiful sunset over snow-capped mountains
/img Futuristic cityscape with flying cars at night
```

### **Utility Commands**

```
/qrcode https://github.com/swadhinbiswas/AIBOT
/urlshortner https://very-long-url-here.com/with/many/parameters
/encrypt "Secret message here"
/iptack 8.8.8.8
```

### **Media Downloads**

```
/twitter https://twitter.com/username/status/1234567890
/webtopdf https://example.com
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Contact & Support

### **Developer**

- **Name:** Swadhin Biswas
- **Telegram:** [@professor_idx](https://t.me/professor_idx)
- **GitHub:** [swadhinbiswas](https://github.com/swadhinbiswas)
- **Email:** swadhinbiswas.dev@gmail.com

### **Project Links**

- **Repository:** [AIBOT on GitHub](https://github.com/swadhinbiswas/AIBOT)
- **Issues:** [Report a Bug](https://github.com/swadhinbiswas/AIBOT/issues)
- **Discussions:** [GitHub Discussions](https://github.com/swadhinbiswas/AIBOT/discussions)

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Pyrogram](https://docs.pyrogram.org/) - Modern Telegram Bot API framework
- [Cloudflare AI](https://developers.cloudflare.com/ai/) - AI model hosting
- [Pollinations AI](https://pollinations.ai/) - Image generation API
- All contributors and users who help improve this project

## 📈 Project Stats

![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https://github.com/swadhinbiswas/AIBOT&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)

## 📸 Demo Screenshots

### Bot Interface

![Bot Interface](<Screenshot from 2024-07-03 01-22-25.png>)

### Features in Action

![AI Image Generation](<Screenshot from 2024-07-03 01-21-51.png>)
![QR Code Generation](<Screenshot from 2024-07-03 01-26-39.png>)
![Utility Commands](<Screenshot from 2024-07-03 01-33-49.png>)

---

<div align="center">

**Made with ❤️ by [Swadhin Biswas](https://github.com/swadhinbiswas)**

⭐ Star this repository if you found it helpful!

</div>
