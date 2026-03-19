from uuid import uuid4, UUID
from datetime import datetime
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.modules.user.dto import CreateUserDTO, UpdateUserDTO
from app.modules.user.user_schema import User

async def get_all_users(db: AsyncIOMotorDatabase) -> list[User]:
    users_collection = db["users"]
    users = []
    async for user in users_collection.find():
        users.append(_format_user(user))
    return users

async def get_user(db: AsyncIOMotorDatabase, user_id: UUID) -> User | None:
    users_collection = db["users"]
    user = await users_collection.find_one({"id": str(user_id)})
    if user:
        return _format_user(user)
    return None

async def create_user(db: AsyncIOMotorDatabase, user_data: CreateUserDTO) -> User:
    users_collection = db["users"]
    new_user = {
        "id": str(uuid4()),
        "name": user_data.name,
        "email": user_data.email,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    await users_collection.insert_one(new_user)
    return _format_user(new_user)

async def update_user(db: AsyncIOMotorDatabase, user_id: UUID, user_data: UpdateUserDTO) -> User | None:
    users_collection = db["users"]
    update_dict = {}
    
    if user_data.name is not None:
        update_dict["name"] = user_data.name
    if user_data.email is not None:
        update_dict["email"] = user_data.email
    
    if not update_dict:
        return await get_user(db, user_id)
    
    update_dict["updated_at"] = datetime.utcnow()
    
    result = await users_collection.find_one_and_update(
        {"id": str(user_id)},
        {"$set": update_dict},
        return_document=True
    )
    
    if result:
        return _format_user(result)
    return None

async def delete_user(db: AsyncIOMotorDatabase, user_id: UUID) -> bool:
    users_collection = db["users"]
    result = await users_collection.delete_one({"id": str(user_id)})
    return result.deleted_count > 0

def _format_user(user_doc: dict) -> User:
    return User(
        id=UUID(user_doc["id"]),
        name=user_doc["name"],
        email=user_doc["email"],
        created_at=user_doc.get("created_at"),
        updated_at=user_doc.get("updated_at")
    )