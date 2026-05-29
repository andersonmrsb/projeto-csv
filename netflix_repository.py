from db import Database

class NetflixRepository:
    def __init__(self):
        self.db = Database()

    def execute_query(self,query,params=()):
        conection = self.db.connect_db()
        cursor = conection.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()
        conection.close()
        return results
    
    