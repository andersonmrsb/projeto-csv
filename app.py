from db import Database
from import_csv import import_csv
from netflix_service import NetflixService

if __name__ == "__main__":
    db = Database()
    conection = db.connect_n()
    db.creat_table()
    sucess = import_csv(conection)  # importa os dados do CSV

    if sucess:
        print("Importação concluída com sucesso!")
        
        service = NetflixService()
        while True:
            options = input(
                "\nEscolha uma opção:\n"
                "1 - Listar todos os títulos disponíveis\n"
                "2 - Listar títulos por tipo (filme ou série)\n"
                "3 - Quantidade de títulos\n"
                "4 - Listar TÍTULOS de cada país\n"
                "5 - Listar anos\n"
                "0 - Sair\n"
            )

            if options == '1':
                for title in service.list_all_titles():
                    print(title)

            elif options == '2':
                content_type = input("Digite o tipo (Movie ou TV Show):\n ")
                if content_type.lower() == 'movie':
                    for title, year, country in service.list_titles_by_type('Movie'):
                        print(f"{title} ({year}) - {country}")
                elif content_type.lower() == 'tv show':
                    for title, year, country in service.list_titles_by_type('TV Show'):
                            print(f"{title} ({year}) - {country}")
                else:
                    print("Tipo inválido. Por favor, escolha 'Movie' ou 'TV Show'.")
                    
            elif options == '3':
                choice = input(f" 1 - Movies / 2 - TV Shows / 3 - Total\n")
                if choice == '1':
                    print(
                        f"Quantidade de filmes: {service.count_titles('Movie')}")
                elif choice == '2':
                    print(
                        f"Quantidade de séries: {service.count_titles('TV Show')}")
                elif choice == '3':
                    print(f"Quantidade total de títulos: {service.count_titles(content_type=None)}")
            
            elif options == '4':
                choice = input(f" listar países: S / N\n")
                if choice.lower() == 's':
                    countries = service.list_countries()
                    print("Países disponíveis:")
                    for i, countrie in enumerate(countries, start=1):
                        print(f"{i}. {countrie}")
                    option = int(input("Digite o número do país desejado: "))
                    if 1 <= option <= len(countries):
                        chosen_country = countries[option - 1]
                        movies = service.list_titles_by_country(chosen_country)
                        print(f"\nTítulos do país: {chosen_country}\n")
                        for title in movies:
                            print(f" - {title}")
                    else:
                        print("Número inválido.")
                    


            elif options == '5':
                years = service.list_years()
                print("Anos disponíveis:")
                for i, year in enumerate(years, start=1):
                        print(f"{i}. {year}")

                escolha_ano = input("Digite o número do ano: ")
                try:
                    chosen_number = int(escolha_ano)
                    if 1 <= chosen_number <= len(years):
                            chosen_year = years[chosen_number - 1]
                            movies = service.titles_by_year(chosen_year)
                            print(f"\nTítulos de {chosen_year}:")
                            for f in movies:
                                print(" ", f)
                    else:
                            print("Número inválido.")
                except ValueError:
                        print("Digite um número válido.")


            elif options == '0':
                print("Saindo do programa.")
                break
    else:
        print("Importação concluída com erros. Verifique os logs para detalhes.")


        
            
            
            
        

        

   