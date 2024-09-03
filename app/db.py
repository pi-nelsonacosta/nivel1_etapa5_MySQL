from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
import os

MONGO_DETAILS = os.getenv("MONGO_DETAILS", "mongodb://localhost:27017")

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.mydatabase  # Reemplaza 'my_database' con el nombre de tu base de datos

def get_database():
    return database
