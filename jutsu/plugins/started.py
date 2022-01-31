

import asyncio

from pyrogram import Client


async def _init() -> None:
    await Client.send_message(-1001661347032, "### SEDEX started !!! ###")


asyncio.get_event_loop().run_until_complete(_init())