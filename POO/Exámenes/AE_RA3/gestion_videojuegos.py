import os
import csv
import json

class Gestion_Videojuegos():


    __team_name = "Team_Name"
    __map_name = "Map_Name"
    __difficulty_level = "Difficulty_Level"
    __points_scored = "Points_Scored"
    __enemies_defeated = "Enemies_Defeated"
    __missions_completed = "Missions_Completed"
    __video_juego = []

    def __init__(self, path):

        try:
            with open(path, mode="r", encoding="utf8") as fich:
                aux = csv.reader(fich)

                # self.__video_juego.append(next(aux))
                next(aux)
                
                for l in aux:
                    self.__video_juego.append(l)

        except IOError as io:
            print("Error IO: ",io)
        except Exception as e:
                print(e)


    def print_lista(self):
        for i in self.__video_juego:
            print(f"{i[0]},{i[1]},{i[2]},{i[3]},{i[4]},{i[5]},{i[6]},{i[7]}")


    def txt_by_cod_equipo(self, codigo_equipo):
        try:
            path = os.path.join(os.path.dirname(__file__),codigo_equipo + ".txt")

            with open(path,"w",encoding="UTF-8") as txt:
                
                lista = []

                for i in self.__video_juego:
                    if i[4] == codigo_equipo:
                        lista.append(i)

                if lista.__len__() > 0:
                    txt.write(f"Resumen del equipo {lista[0][3]}:\n")

                    for l in lista:
                        # txt.write(f"{l[0]},{l[1]},{l[2]},{l[30]},{l[4]},{l[5]},{l[6]},{l[7]}")
                        linea = f"{l[0]},{l[1]},{l[2]},{l[3]},{l[4]},{l[5]},{l[6]},{l[7]}\n"
                        txt.write(linea)

        except Exception as e:
                print(e)

    def read_txt(self, codigo_equipo):

        path = os.path.join(os.path.dirname(__file__),codigo_equipo + ".txt")

        with open(path,"r",encoding="UTF-8") as txt:
                texto = txt.read()
                print(texto)


    def muestra_total(self, nivel):
        total = 0

        for i in self.__video_juego:
            if i[1] == nivel:
                total += int(i[5])
        
        print(f"Total nivel {nivel} = {total}")

    # def get_team_max(self):

    #     list_team = []
        
    #     for i in self.__video_juego:
    #         if i[3] in list_team:
    #             list_team[i[3]] = 2
    #         else:
    #             list_team.append([i[3],1])

   
        