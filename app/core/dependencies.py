from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from app.core.config import settings

mongo_client: AsyncIOMotorClient = None
mongo_db: AsyncIOMotorDatabase = None

async def get_db() -> AsyncIOMotorDatabase:
    return mongo_db