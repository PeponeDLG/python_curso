from partido import Partido
import datetime as dtm

class Partido_Tenis(Partido):
    __DEPORTE="Tenis"

    def __init__(self, jugador_1:str, jugador_2:str, fecha:str, campeonato:str, puntos_jugador_1:list[int], puntos_jugador_2:list[int]):
        try:
            # validación de sets
            if (len(puntos_jugador_1) < 3 or len(puntos_jugador_1) > 5) or (len(puntos_jugador_2) < 3 or len(puntos_jugador_2) > 5):
                raise Exception("El número de sets tiene que estar entre 3 y 5")
            
            if len(puntos_jugador_1) != len(puntos_jugador_2):
                raise Exception("Los dos jugadores deben tener el mismo número de sets")


            self.valida_sets(jugador_1, jugador_2, puntos_jugador_1,puntos_jugador_2)

            super().__init__(jugador_1, jugador_2, fecha, Partido_Tenis.__DEPORTE)
            
            self.__puntos_jugador_1 = puntos_jugador_1
            self.__puntos_jugador_2 = puntos_jugador_2
            self.campeonato = campeonato

        except Exception as e:
            print(e)

    # Implementación métodos abstractos
    def ganador(self):      
        pass

    
    def resultado(self):
        pass

    def representacion(self):
        pass


    # VALIDACIONES
    def validar_fecha(self, fecha:str) -> bool:
        try:
            fecha_aux = dtm.datetime.strptime(fecha,"%d-%m-%Y")
            
            return True
        except Exception as e:
            return False
    
    def none_vacio(self, cadena):
        return len(cadena.strip()) == 0

    def valida_sets(self,jugador_1:str, jugador_2:str, sets_1:list[int], sets_2:list[int]):
        ganados_1 = 0
        ganados_2 = 0
        contador = 0

        for i in range(0,len(sets_1)):
            if contador == 3 and (ganados_1 == 3 or ganados_2 == 3 and ganados_1 != ganados_2): # Si ha pasado de 3 ganando
                jugador_aux = ""
                if ganados_1 > ganados_2: # Coge el nombre del jugador que iba ganando en el conteo erróneo
                    jugador_aux = jugador_1
                else:
                    jugador_aux = jugador_2
                    
                raise Exception(f"El resultado es inválido, el jugador {jugador_aux} ha ganado por 3 sets")

            if sets_1[i] > sets_2[i]: # Cuenta los juegos para cada jugador
                ganados_1 += 1
            else:
                ganados_2 += 1
            
            contador += 1
            
            