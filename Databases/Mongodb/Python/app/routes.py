from flask import Blueprint
from models import db

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def home():
    collection = db.connect().get_collection("mycollection")
    return f"Connected to MongoDB! Found {collection.count_documents({})} documents"
    