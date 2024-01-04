from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bot import TelegramBot
from bot.config import Telegram
from bot.modules.static import *

@TelegramBot.on_message(
    filters.command('start')
    & (
        filters.private |
        filters.group
    )
)
async def start_command(_, msg: Message):
    return await msg.reply(
        text=WelcomeText % {'first_name': msg.from_user.first_name if msg.from_user else 'Anonymous'},
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text='Add me to chat', url=f'https://t.me/{Telegram.BOT_USERNAME}?startgroup=botstart')
                ],
                [
                    InlineKeyboardButton(text='Source Code', url='https://github.com/TheCaduceus/TG-ReactionBot')
                ]
            ]
        )
    )

@TelegramBot.on_message(
    filters.command('emojis')
    & (
        filters.private |
        filters.group
    )
)
async def send_emojis(_, msg: Message):
    return await msg.reply(
        text=SupportedEmojisText,
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text='Reference', url='https://github.com/TheCaduceus/TG-ReactionBot/blob/main/bot/config.py#L8')
                ]
            ]
        )
    )
