

from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

from DaisyXMusic.config import MONGO_URI
from typing import Dict, List, Union

mongo_client = MongoClient(MONGO_URI)
db = mongo_client.daisy

musicdb = db.musicdb

async def is_music_on(chat_id: int) -> bool:
    chat = await musicdb.find_one({"chat_id": chat_id})
    if not chat:
        return False
    return True


async def music_on(chat_id: int):
    is_music = await is_music_on(chat_id)
    if is_music:
        return
    return await musicdb.insert_one({"chat_id": chat_id})


async def music_off(chat_id: int):
    is_music = await is_music_on(chat_id)
    if not is_music:
        return
    return await musicdb.delete_one({"chat_id": chat_id})
