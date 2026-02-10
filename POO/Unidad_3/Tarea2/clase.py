import os
import csv

class app_movil():
    @staticmethod
    def get_csv(path, modelo):
        lista = []

        with open(path,mode="r",encoding="utf8") as fich:
            aux = csv.reader(fich)

            lista.append(next(aux))

            i = lista[0].index("Device Model")
            
            for l in aux:
                if l[i] == modelo:
                    lista.append(l)
        
        return lista
    
    @staticmethod
    def get_dict_num_os(path):
        with open(path,mode="r",encoding="utf8") as fich:
            aux = csv.DictReader(fich)

            os_cache = {}

            for l in aux:
                if l["Operating System"] in os_cache and os_cache[l["Operating System"]] > 0:
                    os_cache[l["Operating System"]] = os_cache[l["Operating System"]] + 1
                else:
                    os_cache[l["Operating System"]] = 1

            return os_cache
        
    @staticmethod
    def get_redux(path):

        with open(path,mode="r",encoding="utf8") as fich:
            aux = csv.reader(fich)
            pathW = os.path.join(os.path.dirname(__file__), "archivos/get_redux.csv")

            lista = []
            lista.append(next(aux))

            a = lista[0].index("App Usage Time (min/day)")
            b = lista[0].index("Gender")

            for l in aux:
                lista.append((l[a],l[b]))

            with open(pathW, mode='w', encoding="utf8", newline='') as archivo:
                csv_writer = csv.writer(archivo, delimiter=',', lineterminator='\n')

                for elemento in lista:
                    csv_writer.writerow(elemento)



class Resultado_juego:
    # Year,Host_country,Host_city,Country_Name,Country_Code,Gold,Silver,Bronze
    def __init__(
        self,
        Year,
        Host_country,
        Host_city,
        Country_Name,
        Country_Code,
        Gold,
        Silver,
        Bronze,
    ):
        self.Year = Year
        self.Host_country = Host_country
        self.Host_city = Host_city
        self.Country_Name = Country_Name
        self.Country_Code = Country_Code
        self.Gold = Gold
        self.Silver = Silver
        self.Bronze = Bronze


class Gestion_Juegos:
    cabeceras = (
        "Year,Host_country,Host_city,Country_Name,Country_Code,Gold,Silver,Bronze"
    )

    def __init__(self, lista: []):
        self.lista = lista

    def get_data_by_country_code(self, pais: str) -> []:
        aux = []

        list_aux = list(filter(lambda x: x.Country_Code.lower() == pais.lower(),self.lista))

        for line in self.lista:
            if line.Country_Code.lower() == pais.lower():
                aux.append(line)

        return aux

    def get_medals_by_country_code_year(self, pais: str, año: str) -> []:
        aux = []

        for line in self.lista:
            if line.Country_Code.lower() == pais.lower() and line.Year == año:
                aux.append(line)

        return aux

    def generate_csv(self,pais: str):
        aux = []

        for line in self.lista:
            if line.Country_Code.lower() == pais.lower():
                aux.append(line)

        path = os.path.join(os.path.dirname(__file__), "resumen_" + pais + ".csv")

        with open(path, mode="w", encoding="utf8", newline='') as fic:
            csv_writer = csv.writer(fic, delimiter=",", lineterminator="\n")

            for elem in aux:
                lista = (
                    elem.Year,
                    elem.Host_country,
                    elem.Host_city,
                    elem.Country_Name,
                    elem.Country_Code,
                    elem.Gold,
                    elem.Silver,
                    elem.Bronze
                )
                csv_writer.writerow(lista)