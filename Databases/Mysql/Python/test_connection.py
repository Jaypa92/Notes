from server import connect_to_db

if __name__ == "__main__":
    db = connect_to_db()
    if db:
        db.close()