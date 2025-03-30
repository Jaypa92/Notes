from pymongo import MongoClient
from flask import current_app

class MongoDB:
    def __init__(self):
        self.client = None
        self.db = None

    def connect(self):
        if not self.client:
            try:
                print("Attempting to connect to MongoDB...")
                self.client = MongoClient(current_app.config["MONGO_URI"])
                self.db = self.client.get_database()
                if self.db is not None:
                    print(f"Connected to MongoDB: {self.db.name}")
                else:
                    print("Failed to connect to MongoDB database")
            except Exception as e:
                print(f"Error connecting to MongoDB: {e}")
        return self.db

db = MongoDB()