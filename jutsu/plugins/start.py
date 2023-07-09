# start.py

from pyrogram import filters

from jutsu import sedex


@sedex.on_message(
    filters.command(["start"], prefixes=";"), group=2
)
async def start_(_, message):
    reply_to = message.message_id
    await sedex.send_message(
        message.chat.id,
        f"Hello **{message.from_user.first_name}**, thank you for using this bot...",
        reply_to_message_id=reply_to
    )
