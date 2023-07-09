# database.py

import asyncio
from typing import List

from motor.motor_asyncio import AsyncIOMotorClient
from motor.core import AgnosticClient, AgnosticDatabase, AgnosticCollection

from jutsu.config import Config

_MGCLIENT: AgnosticClient = AsyncIOMotorClient(Config.DB_URL)
# _RUN = asyncio.get_event_loop().run_until_complete

_DATABASE: AgnosticDatabase = _MGCLIENT['jutsu']
_COL_LIST: List[str] = _DATABASE.list_collection_names()


def get_collection(name: str) -> AgnosticCollection:
    """ create or get collection from database """
    return _DATABASE[name]

def _close_db() -> None:
    _MGCLIENT.close()

CHATS = get_collection("CHATS")
