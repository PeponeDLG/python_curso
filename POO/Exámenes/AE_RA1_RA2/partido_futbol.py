from partido import Partido
import datetime as dtm

class Partido_Futbol(Partido):
    __DEPORTE="Fútbol"

    def __init__(self, equipo_1:str, equipo_2:str, fecha:str, goles_equipo_1:int = 0, goles_equipo_2:int = 0):
        try:
            if goles_equipo_1 < 0 or goles_equipo_2 < 0:
                raise ValueError("Los goles no pueden ser negativos")
            
            super().__init__(equipo_1, equipo_2, fecha, Partido_Futbol.__DEPORTE)
            
            self.__goles_equipo_1 = goles_equipo_1
            self.__goles_equipo_2 = goles_equipo_2
        except Exception as e:
            print(e)

    # Implementación métodos abstractos
    def ganador(self):
        if self.__goles_equipo_1 == self.__goles_equipo_2:
            return f"Ha sido empate"
        elif self.__goles_equipo_1 < self.__goles_equipo_2:
            return f"El ganador es{super().get_equipo_1}"
        elif self.__goles_equipo_1 > self.__goles_equipo_2:
            return f"El ganador es{super().get_equipo_2}"

    
    def resultado(self):
        return f"{super().get_equipo_1} {self.__goles_equipo_1} - {self.__goles_equipo_2} {super().get_equipo_2}"

    
    def representacion(self):
        return f"{super().get_equipo_1} Vs. {super().get_equipo_2} - {super().get_fecha} - {super().get_tipo_competicion}"


    # VALIDACIONES
    def validar_fecha(self, fecha:str) -> bool:
        try:
            fecha_aux = dtm.datetime.strptime(fecha,"%d-%m-%Y")
            
            return True
        except Exception as e:
            return False
    
    def none_vacio(self, cadena):
        return len(cadena.strip()) == 0