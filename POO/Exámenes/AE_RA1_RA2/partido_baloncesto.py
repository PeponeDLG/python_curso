from partido import Partido
import datetime as dtm

class Partido_Baloncesto(Partido):
    __DEPORTE="Baloncesto"

    def __init__(self, equipo_1:str, equipo_2:str, fecha:str, puntos_equipo_1:int = 0, puntos_equipo_2:int = 0):
        try:
            if puntos_equipo_1 < 0 or puntos_equipo_2 < 0:
                raise Exception("Los puntos no pueden ser negativos")
            elif puntos_equipo_1 == puntos_equipo_2:
                raise Exception("El resultado no puede ser un empate")

            super().__init__(equipo_1, equipo_2, fecha, Partido_Baloncesto.__DEPORTE)
            
            self.__puntos_equipo_1 = puntos_equipo_1
            self.__puntos_equipo_2 = puntos_equipo_2

        except Exception as e:
            print(e)

    # Implementación métodos abstractos
    def ganador(self):
        if self.__puntos_equipo_1 == self.__puntos_equipo_2:
            return f"Ha sido empate"
        elif self.__puntos_equipo_1 < self.__puntos_equipo_2:
            return f"El ganador es{super().get_equipo_1}"
        elif self.__puntos_equipo_1 > self.__puntos_equipo_2:
            return f"El ganador es{super().get_equipo_2}"

    
    def resultado(self):
        return f"{self.__puntos_equipo_1}  {super().get_equipo_1} - {super().get_equipo_2} {self.__puntos_equipo_2}"
    
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