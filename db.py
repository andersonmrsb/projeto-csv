import sqlite3

class Database:
    def __init__(self, db_name="netflix.db"):
        self.db_name = db_name

    def conectar(self):
        return sqlite3.connect(self.db_name)

    def criar_tabela(self):
        conexao = self.conectar()
        cursor = conexao.cursor()
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
        conexao.commit()