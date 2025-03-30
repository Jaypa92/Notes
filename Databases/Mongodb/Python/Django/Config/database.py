from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

try:
    client = MongoClient(MONGO_URI)
    client.admin.command("ping")
    print("MongoDB Connected:", client.server_info()["version"])

except Exception as e :
    print("MongoDB Connection Failed:", e)