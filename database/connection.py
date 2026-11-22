import os
import sqlite3

def get_connection():
    db_path = os.path.join("database", "joao.db")
    return sqlite3.connect(db_path)