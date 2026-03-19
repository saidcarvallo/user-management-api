from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

class User(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    created_at: datetime | None = None
    updated_at: datetime | None = None