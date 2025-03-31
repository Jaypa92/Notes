import mysql.connector
from config import DB_CONFIG

def connect_to_db():
    try:
        db = mysql.connector.connect(**DB_CONFIG)
        print("Successfully connected to MySQL")
        return db
    except mysql.connector.Error as err:
        pring(f"Error Connecting to MySQL:{err}")
        return None