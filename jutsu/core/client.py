# client.py

from pyrogram import Client

from .. import config


class Sedex(Client):

    def __init__(self):
        kwargs = {
            'name': 'SedexBot',
            'api_id': config.Config.API_ID,
            'api_hash': config.Config.API_HASH,
            'bot_token': config.Config.BOT_TOKEN,
            'in_memory': True,
            'plugins': dict(root='jutsu/plugins')
        }
        super().__init__(**kwargs)
