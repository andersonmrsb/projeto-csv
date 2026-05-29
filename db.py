import sqlite3

import os
from dotenv import load_dotenv

load_dotenv()


class Database:
    def __init__(self):
        self.DB_NAME = os.getenv("DB_NAME", "netflix.db")

    def connect_db(self):
        return sqlite3.connect(self.DB_NAME)

    def create_table(self):
        conection = self.connect_db()
        cursor = conection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS netflix (
            show_id TEXT PRIMARY KEY,
            type TEXT,
            title TEXT,
            director TEXT,
            cast TEXT,
            country TEXT,
            date_added TEXT,
            release_year INTEGER,
            rating TEXT,
            duration TEXT,
            listed_in TEXT,
            description TEXT
        )
    ''')
        conection.close()

