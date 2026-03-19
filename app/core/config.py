from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # In Kubernetes, use the mongo service DNS name.
    # Locally you can override setting in a .env file (e.g. MONGO_URL="mongodb://localhost:27017/")
    MONGO_URL: str = "mongodb://mongo-service:27017/"
    MONGO_DB_NAME: str = "usuarios_db"
    MONGO_USERS_COLLECTION: str = "users"

    class Config:
        env_file = ".env"

settings = Settings()