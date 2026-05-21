from db import Database

class NetflixRepository:
    def __init__(self):
        self.db = Database()

    def executar_query(self,query,params=()):
        conexao = self.db.conectar()
        cursor = conexao.cursor()
        cursor.execute(query, params)
        resultados = cursor.fetchall()
        conexao.close()
        return resultados
    
    