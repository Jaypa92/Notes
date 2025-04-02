import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname = os.getenv("DB_NAME"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            host = os.getenv("DB_HOST"),
            port= os.getenv("DB_PORT")
        )

        print("Successfully connected to PostgreSQL")
        conn.close()
    except Exception as e:
        print(f"Connection failed:{e}")