from pyrogram import filters
from pyrogram.types import Message
from random import choice

from bot import TelegramBot, logger
from bot.config import Telegram

@TelegramBot.on_message(filters.all)
async def send_reaction(_, msg: Message):
    await msg.react(choice(Telegram.EMOJIS))

logger.info("Bot is now started.")