from fastapi import APIRouter, HTTPException, Depends
from uuid import UUID
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.modules.user import user_service
from app.modules.user.dto import CreateUserDTO, UpdateUserDTO
from app.modules.user.user_schema import User
from app.core.dependencies import get_db

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/", response_model=list[User])
async def get_users(db: AsyncIOMotorDatabase = Depends(get_db)):
    return await user_service.get_all_users(db)

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: UUID, db: AsyncIOMotorDatabase = Depends(get_db)):
    user = await user_service.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/", response_model=User, status_code=201)
async def create_user(user_data: CreateUserDTO, db: AsyncIOMotorDatabase = Depends(get_db)):
    return await user_service.create_user(db, user_data)

@router.put("/{user_id}", response_model=User)
async def update_user(user_id: UUID, user_data: UpdateUserDTO, db: AsyncIOMotorDatabase = Depends(get_db)):
    updated_user = await user_service.update_user(db, user_id, user_data)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/{user_id}", status_code=204)
async def delete_user(user_id: UUID, db: AsyncIOMotorDatabase = Depends(get_db)):
    success = await user_service.delete_user(db, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return None

