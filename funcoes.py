from reposit import NetflixRepository


class NetflixService:
    def __init__(self):
        self.repo = NetflixRepository()

    class Service:
        def __init__(self, repo):
            self.repo = repo

    # 1 - já funcionando: listar todos os títulos
    def listar_todos_titulos(self):
        resultados = self.repo.executar_query("SELECT title FROM netflix")
        if resultados:
            return [linha[0] for linha in resultados]
            return []

    # 2 - listar títulos por tipo (Movie ou TV Show)
    def listar_titulos_com_info(self, tipo):
        return self.repo.executar_query(
            "SELECT title, release_year, country FROM netflix WHERE type = ?",
            (tipo,)
        )

    # 3 - quantidade de títulos
    def quantidade_titulos(self, tipo=None):
        query = "SELECT COUNT(*) FROM netflix WHERE type = ?" if tipo else "SELECT COUNT(*) FROM netflix"
        params = (tipo,) if tipo else ()
        resultado = self.repo.executar_query(query, params)
        return resultado[0][0] if resultado else 0

    def total_titulos(self):
        resultado = self.repo.executar_query("SELECT COUNT(*) FROM netflix")
        return resultado[0][0] if resultado else 0

    # 4 - listar filmes de cada país

    def listar_paises(self):
        # DISTINCT evita repetição de países
        query = "SELECT country FROM netflix WHERE country != '' AND country != 'Desconhecido' ORDER BY country"
        resultados = self.repo.executar_query(query)
        paises = []
        for linha in resultados:
            if linha[0]:
                for pais in linha[0].split(","):
                    paises.append(pais.strip())
    # Remove duplicados usando set e ordena
        paises_unicos = sorted(set(paises))
        return sorted(paises_unicos)

    def pais_desejado(self, pais):
        query = "SELECT title FROM netflix WHERE country LIKE ?"
        resultados = self.repo.executar_query(query, (f"%{pais}%",))
        return [linha[0] for linha in resultados] if resultados else []

    # 5 - listar filmes de cada ano

    def listar_anos(self):
        query = "SELECT DISTINCT release_year FROM netflix WHERE release_year IS NOT NULL ORDER BY release_year"
        resultados = self.repo.executar_query(query)
        return [linha[0] for linha in resultados] if resultados else []

    def 
    (self, ano):
        query = "SELECT title FROM netflix WHERE release_year = ?"
        resultados = self.repo.executar_query(query, (ano,))
        return [linha[0] for linha in resultados] if resultados else []