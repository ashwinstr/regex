# help.py

from pyrogram import filters

from jutsu import sedex


@sedex.on_message(
    filters.command(["help_"], prefixes=";"), group=1
)
async def helper(bot, message):
    reply_to = message.message_id
    help_ = f"""
__Hello there__ **{message.from_user.first_name}**__, this is the Sedex bot.__

**USAGE:**
__Replace any part of the target message to have fun with friends...__

**HOW:**
__To use this bot, you need to send command with reply to the targeted message.__
`a/text that will be replaced/text that will replace`

**Note:** __To not auto-delete the command message use__ `-n` __at the end of the command.__

**EXAMPLE:**
__Reply to a message with text as "Hi, nice to meet you." with__
`a/Hi/Bye`

__For more help_ or to learn from regexone, go__ **[here](www.regexone.com)**
__Or from regexr, go__ **[here](www.regexr.com).**

__Good luck.__
"""
    await sedex.send_message(
        message.chat.id,
        help_,
        reply_to_message_id=reply_to,
        disable_web_page_preview=True
    )
