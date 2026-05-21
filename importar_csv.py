import csv 
from pydantic import ValidationError
from valid import Netflix

def import_csv(conexao, caminho_csv="netflix_titles.csv"):
    cursor = conexao.cursor()
    sucesso = True

    with open(caminho_csv, 'r', encoding='utf-8-sig') as arquivo:
        arquivo_csv = csv.DictReader(arquivo)
        for row in arquivo_csv:
            try:
                registro = Netflix(**row)
                cursor.execute('''
                    INSERT OR REPLACE INTO netflix 
                    (show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description)
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
                ''', tuple(row.values()))
            except ValidationError as e:
                print(f"Erro de validação para o registro {row['show_id']}: {e}")
                sucesso = False

    conexao.commit()
    return sucesso
