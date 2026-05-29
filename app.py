from db import Database
from import_csv import import_csv
from netflix_service import NetflixService

if __name__ == "__main__":
    db = Database()
    conection = db.connect_db()
    db.create_table()
    success = import_csv(conection)  # importa os dados do CSV

    if success:
        print("Importação concluída com sucesso!")
        
service = NetflixService()
        


        
            
            
            
        

        

   