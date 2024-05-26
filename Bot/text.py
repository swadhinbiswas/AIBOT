import logging
import asyncio
from telegram import ForceReply, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler,filters,ApplicationBuilder

import os
import requests

ACCOUNT_ID = "0ddd9358ccb8fd61c7f19b3ded0395ef"
AUTH_TOKEN = "ZGpOQRCTTRBBpEcnplx7gN_9MfEvfddSpzngykmZ"

def texttotext(text):
    response = requests.post(
      f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@hf/google/gemma-7b-it",
        headers={"Authorization": f"Bearer {AUTH_TOKEN}"},
        json={
          "messages": [
            {"role": "system", "content": "You are a friendly assistant"},
            {"role": "user", "content": text}
          ]
        }
    )
    result = response.json()
    return result['result']['response']




app=ApplicationBuilder().token("6495322558:AAGkkAdzQMGPbt3EktAZ5a-jNMhQGz7MN74").build()

async def start(update: Update, context: ContextTypes) -> None:
    replay_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Yes", callback_data="yes"), InlineKeyboardButton("No", callback_data="no")]])
    await update.message.reply_text('replay_markup', reply_markup=replay_markup)
    
async def help_command(update: Update, context: ContextTypes) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text('Help!')
    

async def echo(update: Update, context: ContextTypes) -> None:
   
    text=update.message.text[4:]
    response=texttotext(text)
    await update.message.reply_text("please wait")
    print(response)
    await update.message.reply_text(response)
    
    



app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

app.run_polling(allowed_updates=Update.ALL_TYPES)
