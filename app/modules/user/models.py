from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

class UserModel(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True