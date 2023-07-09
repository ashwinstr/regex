# client.py

from pyrogram import Client

from ..config import Config
from ..plugins.start import _init


class Sedex(Client):

    def __init__(self):
        kwargs = {
            'name': 'SedexBot',
            'api_id': Config.API_ID,
            'api_hash': Config.API_HASH,
            'bot_token': Config.BOT_TOKEN,
            'in_memory': True,
            'plugins': dict(root='jutsu/plugins')
        }
        super().__init__(**kwargs)
		
    async def start(self: 'Sedex'):
	await super().start()
	await self.send_message(Config.LOG_CHANNEL_ID, "`Sedex has been started...`")
        await _init()
