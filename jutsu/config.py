# config.py

import os
from typing import List
from dotenv import load_dotenv

if os.path.isfile("config.env"):
	load_dotenv("config.env")


class Config:

    API_HASH = os.environ.get("API_HASH")
    API_ID = int(os.environ.get("API_ID", 0))
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    CHATS: List[int] = []
    DB_URL = os.environ.get("DB_URL")
    LOG_CHANNEL_ID = int(os.environ.get("LOG_CHANNEL_ID", 0))
    OWNER_ID = int(os.environ.get("OWNER_ID", 0))
