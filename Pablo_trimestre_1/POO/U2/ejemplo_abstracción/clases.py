# Importación necesaria para crear clases abstractas
from abc import ABC, abstractmethod

# clase abstracta
class Empleado(ABC):
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    # Método abstracto. No hace nada y ha de ser sobreescrita por las clases hijas
    @abstractmethod
    def get_info(self):
        pass

class Director(Empleado):
    def __init__(self, nombre, salario, bono):
        super().__init__(nombre, salario)
        self.bono = bono

    def get_info(self):
        return (
            f"Nombre: {self.nombre}, Salario: {self.salario}, "
            f"Bono: {self.bono}"
        )

class Vendedor(Empleado):
    def __init__(self, nombre, salario, comision):
        super().__init__(nombre, salario)
        self.comision = comision

    def get_info(self):
        return (
            f"Nombre: {self.nombre}, Salario: {self.salario}, "
            f"Comisión: {self.comision}"
        )