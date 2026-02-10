class Coche:
    
    def __init__(self, marca, modelo, anio, kilometros):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometros = kilometros

    def get_info(self):
        info = f"{self.marca} {self.modelo} ({self.anio}) - {self.kilometros} km"
        return info

    def get_instance_values(self):
        instance_values = f"Coche({self.marca}, {self.modelo}, {self.anio}, {self.kilometros})"
        return instance_values

    # Método mágico para comparar instancias
    def __eq__(self, other):
        # Primero comprueba que ambos objetos sean de la misma clase
        if not isinstance(other, Coche):
            return NotImplemented
        # Compara los atributos y devuelve True o False
        is_equal = True

        if self.marca != other.marca:
            is_equal = False

        if self.modelo != other.modelo:
            is_equal = False

        if self.anio != other.anio:
            is_equal = False

        if self.kilometros != other.kilometros:
            is_equal = False

        return is_equal

    # Elimina un objeto y muestra un mensaje
    def remove_instance(self):
        del self
        print("El coche ha sido eliminado con éxito.")
