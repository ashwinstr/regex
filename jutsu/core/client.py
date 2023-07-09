# client.py

import asyncio
import os
import importlib

from pyrogram import Client

from jutsu.config import Config
from jutsu.core.database import _close_db

async def _init_func():
	init_list_ = []
	plug_list = os.listdir("jutsu/plugins")
	for one in plug_list:
		path_ = one.replace("/", ".")
		imported_ = importlib.import_module(path_)
		if not hasattr(imported_, "_init"):
			continue
		init_function = getattr(imported_, "_init")
		init_list_.append(init_function())
	try:
		await asyncio.gather(*init_list_)
	except ConnectionError:
		print("Connection error.")
	except BaseException as e:
		print(f"Error in an init function: `{e}`")
	init_list_.clear()


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

	async def start(self):
		await super().start()
		await self.send_message(Config.LOG_CHANNEL_ID, "`Sedex has been started...`")
		await _init_func()

	async def stop(self, block: bool = True):
		_close_db()
		await super().stop(block=block)
