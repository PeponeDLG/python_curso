from abc import ABC, abstractmethod
import datetime as dtm

class Partido(ABC):
    
    # Histórico de los partidos jugados
    PARTIDOS_EQ1_HIST:list[str] = []
    PARTIDOS_EQ2_HIST:list[str] = []
    PARTIDOS_FEC_HIST:list[str] = []

    def __init__(self, equipo_1:str, equipo_2:str, fecha:str, tipo_competicion:str):
        try:
            # Validaciones de los parámetros de entrada
            if self.none_vacio(equipo_1) or self.none_vacio(equipo_2):
                raise ValueError("El nombre de los equipos son obligatorios")
            elif self.none_vacio(fecha):
                raise ValueError("La fecha es obligatoria")
            elif self.validar_fecha(fecha) == False:
                raise ValueError("La fecha debe terner el formato DD-MM-YYYY")
            elif self.none_vacio(tipo_competicion):
                raise ValueError("El tipo de competición es obligatorio")

            # Asignación de valores de instancia
            self.__equipo_1 = equipo_1
            self.__equipo_2 = equipo_2
            self.__fecha = fecha
            self.__tipo_competicion = tipo_competicion

            # Asignación de valores de clase
            Partido.PARTIDOS_EQ1_HIST.append(equipo_1)
            Partido.PARTIDOS_EQ2_HIST.append(equipo_2)
            Partido.PARTIDOS_FEC_HIST.append(fecha)
        except Exception as e:
            print(e)

    # Métodos Abstractos

    @abstractmethod
    def ganador(self):
        pass

    @abstractmethod
    def resultado(self):
        pass

    @abstractmethod
    def representacion(self):
        pass

    # Métodos de instancia

    def comprobar_partidos(self, equipo_1:str, equipo_2:str, fecha:str) -> bool:
        try:
            if self.validar_fecha(fecha) == False:
                raise ValueError("La fecha debe terner el formato DD-MM-YYYY")
            elif self.none_vacio(equipo_1) or self.none_vacio(equipo_2):
                raise ValueError("Es obligatorio el nombre de los dos equipos")

            index_fecha_aux:list[int] = [] # Guardará los indices del histórico de las fechas de los partidos que sean similares a la que venga por parámetro

            # Recopila los índices de las fechas coincidentes
            for i in range(0,len(Partido.PARTIDOS_FEC_HIST)):
                if  Partido.PARTIDOS_FEC_HIST[i] == fecha:
                    index_fecha_aux.append(i)

            # Si ha encontrado fechas coincidentes, busca si hay un partido coincidente en esas posicioes
            if len(index_fecha_aux) > 0:
                for i in index_fecha_aux:
                    eq1_aux = Partido.PARTIDOS_EQ1_HIST[i]
                    eq2_aux = Partido.PARTIDOS_EQ2_HIST[i]
                    fec_aux = Partido.PARTIDOS_FEC_HIST[i]

                    if eq1_aux.upper() == equipo_1.upper() and eq2_aux.upper() == equipo_2.upper() and fec_aux == fecha:
                        print(f"Este partido {equipo_1} Vs. {equipo_2} del día {fecha} ya ha sido disputado.")
                        break
            else:
                print(f"El partido {equipo_1} Vs. {equipo_2} del día {fecha} NO se ha disputado todavía.")

            return True
        except Exception as e:
            print(e)

    # Getters
    @property
    def get_equipo_1(self):
        return self.__equipo_1
    
    @property
    def get_equipo_2(self):
        return self.__equipo_2

    @property
    def get_fecha(self):
        return self.__fecha

    @property
    def get_tipo_competicion(self):
        return self.__tipo_competicion

    # VALIDACIONES
    def validar_fecha(self, fecha:str) -> bool:
        try:
            fecha_aux = dtm.datetime.strptime(fecha,"%d-%m-%Y")
            
            return True
        except Exception as e:
            return False
    
    def none_vacio(self, cadena):
        return len(cadena.strip()) == 0