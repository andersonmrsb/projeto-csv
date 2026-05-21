from nbclient import execute
from db import Database
from importar_csv import import_csv
from funcoes import NetflixService

if __name__ == "__main__":
    db = Database()
    conexao = db.conectar()
    db.criar_tabela()
    sucesso = import_csv(conexao)  # importa os dados do CSV

    if sucesso:
        print("Importação concluída com sucesso!")
    else:
        print("Importação concluída com erros. Verifique os logs para detalhes.")

service = NetflixService()

while True:
    opcoes = input(
        "\nEscolha uma opção:\n"
        "1 - Listar todos os títulos disponíveis\n"
        "2 - Listar títulos por tipo (filme ou série)\n"
        "3 - Quantidade de títulos\n"
        "4 - Listar TÍTULOS de cada país\n"
        "5 - Listar anos\n"
        "0 - Sair\n"
    )

    if opcoes == '1':
        for titulo in service.listar_todos_titulos():
            print(titulo)

    elif opcoes == '2':
        tipo = input("Digite o tipo (Movie ou TV Show):\n ")
        if tipo == 'Movie':
            for titulo, ano, pais in service.listar_titulos_com_info('Movie'):
                print(f"{titulo} ({ano}) - {pais}")
        else:
            for titulo, ano, pais in service.listar_titulos_com_info('TV Show'):
                print(f"{titulo} ({ano}) - {pais}")

    elif opcoes == '3':
        escolha = input(f" 1 - Movies / 2 - TV Shows / 3 - Total\n")
        if escolha == '1':
            print(
                f"Quantidade de filmes: {service.quantidade_titulos('Movie')}")
        elif escolha == '2':
            print(
                f"Quantidade de séries: {service.quantidade_titulos('TV Show')}")
        elif escolha == '3':
            print(f"Quantidade total de títulos: {service.total_titulos()}")

    elif opcoes == '4':
        escolha = input(f" listar países: S / N\n")
        if escolha.lower() == 's':
            paises = service.listar_paises()
            print("Países disponíveis:")
            for i, pais in enumerate(paises, start=1):
                print(f"{i}. {pais}")
            opcao = int(input("Digite o número do país desejado: "))
            if 1 <= opcao <= len(paises):
                pais_escolhido = paises[opcao - 1]
                filmes = service.pais_desejado(pais_escolhido)
                print(f"\nTítulos do país: {pais_escolhido}\n")
                for titulo in filmes:
                    print(f" - {titulo}")
            else:
                print("Número inválido.")
             


    elif opcoes == '5':
        anos = service.listar_anos()
        print("Anos disponíveis:")
        for i, ano in enumerate(anos, start=1):
                print(f"{i}. {ano}")

        escolha_ano = input("Digite o número do ano: ")
        try:
            n_escolhido = int(escolha_ano)
            if 1 <= n_escolhido <= len(anos):
                    ano_escolhido = anos[n_escolhido - 1]
                    filmes = service.titulos_por_ano(ano_escolhido)
                    print(f"\nTítulos de {ano_escolhido}:")
                    for f in filmes:
                        print(" ", f)
            else:
                    print("Número inválido.")
        except ValueError:
                print("Digite um número válido.")


    elif opcoes == '0':
        print("Saindo do programa.")
        break
            
            
            
        

        

   