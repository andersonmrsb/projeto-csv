from db import Database

class NetflixRepository:
    def __init__(self):
        self.db = Database()

    def execut_query(self,query,params=()):
        conection = self.db.connect_n()
        cursor = conection.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()
        conection.close()
        return results
    
    