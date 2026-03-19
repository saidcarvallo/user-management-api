from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from app.routers.api_router import api_router
from app.core.config import settings
from app.core import dependencies

app = FastAPI()

app.include_router(api_router)

@app.on_event("startup")
async def startup_event():
    dependencies.mongo_client = AsyncIOMotorClient(settings.MONGO_URL)
    dependencies.mongo_db = dependencies.mongo_client[settings.MONGO_DB_NAME]
    print("Connected to MongoDB")

@app.on_event("shutdown")
async def shutdown_event():
    dependencies.mongo_client.close()
    print("Disconnected from MongoDB")

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Expiry API!"}