# start.py

from pyrogram import filters
from pyrogram.types import Message

from jutsu import sedex, Config, Collection

CHATS = Collection.CHATS

async def _init() -> None:
    """ load chats' list at start """
    Config.CHATS.clear()
    async for one in CHATS.find():
        Config.CHATS.append(one['_id'])
        


@sedex.on_message(
    filters.command(["start"], prefixes=";"), group=2
)
async def start_(_, message: Message):
    reply_to = message.id
    await sedex.send_message(
        message.chat.id,
        f"Hello **{message.from_user.first_name}**, thank you for using this bot...",
        reply_to_message_id=reply_to
    )
