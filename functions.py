from reposit import NetflixRepository


class NetflixService:
    def __init__(self):
        self.repo = NetflixRepository()

    class Service:
        def __init__(self, repo):
            self.repo = repo

    # 1 - já funcionando: listar todos os títulos
    def list_all_titles(self):
        results = self.repo.execut_query("SELECT title FROM netflix")
        if results:
            return [line[0] for line in results]
            return []

    # 2 - listar títulos por tipo (Movie ou TV Show)
    def list_titles_by_type(self, type):
        return self.repo.execut_query(
            "SELECT title, release_year, country FROM netflix WHERE type = ?",
            (type,)
        )

    # 3 - quantidade de títulos
    def count_titles(self, type=None):
        query = "SELECT COUNT(*) FROM netflix WHERE type = ?" if type else "SELECT COUNT(*) FROM netflix"
        params = (type,) if type else ()
        result = self.repo.execut_query(query, params)
        return result[0][0] if result else 0

    def total_titles(self):
        result = self.repo.execut_query("SELECT COUNT(*) FROM netflix")
        return result[0][0] if result else 0

    # 4 - listar filmes de cada país

    def list_countries(self):
        # DISTINCT evita repetição de países
        query = "SELECT country FROM netflix WHERE country != '' AND country != 'Desconhecido' ORDER BY country"
        results = self.repo.execut_query(query)
        countries = []
        for line in results:
            if line[0]:
                for country in line[0].split(","):
                    countries.append(country.strip())
    # Remove duplicados usando set e ordena
        unique_countries = sorted(set(countries))
        return sorted(unique_countries)

    def desired_country(self, country):
        query = "SELECT title FROM netflix WHERE country LIKE ?"
        results = self.repo.execut_query(query, (f"%{country}%",))
        return [line[0] for line in results] if results else []

    # 5 - listar filmes de cada ano

    def list_years(self):
        query = "SELECT DISTINCT release_year FROM netflix WHERE release_year IS NOT NULL ORDER BY release_year"
        results = self.repo.execut_query(query)
        return [line[0] for line in results] if results else []

    def titles_by_year(self, ano):
        query = "SELECT title FROM netflix WHERE release_year = ?"
        results = self.repo.execut_query(query, (ano,))
        return [line[0] for line in results] if results else []
