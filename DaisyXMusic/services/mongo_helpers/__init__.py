# Support Dual Mongo DB now
# For free users

from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

from DaisyX.config import MONGO_URI

mongo_client = MongoClient(MONGO_URI)
db = mongo_client.daisy
