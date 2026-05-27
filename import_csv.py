import csv 
from pydantic import ValidationError
from netflix_model import Netflix

def import_csv(conexao, caminho_csv="netflix_titles.csv"):
    cursor = conexao.cursor()
    sucess = True

    with open(caminho_csv, 'r', encoding='utf-8-sig') as file:
        file_csv = csv.DictReader(file)
        for row in file_csv:
            try:
                record = Netflix(**row)
                cursor.execute('''
                    INSERT OR REPLACE INTO netflix
                    (show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description)
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
                ''',(
                    record.show_id, record.type, record.title, record.director,
                    record.cast, record.country, record.date_added, record.release_year,
                    record.rating, record.duration, record.listed_in, record.description
                ))
            except ValidationError as e:
                print(f"Erro de validação para o registro {row['show_id']}: {e}")
                sucess = False

    conexao.commit()
    return sucess
