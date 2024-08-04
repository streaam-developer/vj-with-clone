# Don't Remove Credit @presood
# Subscribe YouTube Channel For Amazing Bot @presood
# Ask Doubt on telegram @presood

from pyrogram import Client, filters
from plugins.Extra.engine import ask_ai


@Client.on_message(filters.command('openai'))
async def openai_ask(client, message):
    if len(message.command) == 1:
       return await message.reply_text("Give an input!")
    m = await message.reply_text("👀")
    await ask_ai(client, m, message)
