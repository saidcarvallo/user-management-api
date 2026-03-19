from pydantic import BaseModel, EmailStr

class CreateUserDTO(BaseModel):
    name: str
    email: EmailStr

class UpdateUserDTO(BaseModel):
    name: str | None = None
    email: EmailStr | None = None