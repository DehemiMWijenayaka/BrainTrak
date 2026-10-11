
from fastapi import FastAPI
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

MONGO_URI = os.getenv("MONGO_URI")

@app.get("/")
def home():
    return {"message": "BrainTrak backend is running"}

@app.get("/health/database")
def database_health():
    if not MONGO_URI:
        return {"status": "error", "message": "MONGO_URI missing in .env"}

    try:
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        client.admin.command("ping")
        return {"status": "success", "message": "MongoDB connected"}
    except PyMongoError as e:
        return {"status": "error", "message": str(e)}