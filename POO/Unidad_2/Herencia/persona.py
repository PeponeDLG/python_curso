# definición de las clases

# clase base
class Persona:
    def __init__(self, nombre, apellidos, correo):
        # Atributos comunes para todas las personas
        self.nombre = nombre
        self.apellidos = apellidos
        self.correo = correo

    def __str__(self):
        # Método que devuelve una representación en texto del objeto
        return f"{self.nombre} {self.apellidos} - {self.correo}"

# clase derivada (hereda de Persona)
class Cliente(Persona):
    def __init__(self, nombre, apellidos, correo, num_cliente, numero_cuenta):
        # Llamamos al constructor de la clase base para inicializar los atributos heredados
        # Persona.__init__(nombre, apellidos, correo)
        super().__init__(nombre, apellidos, correo)
        # Nuevos atributos específicos de Cliente
        self.num_cliente = num_cliente
        self.numero_cuenta = numero_cuenta

    def __str__(self):
        # Sobrescribimos __str__ para mostrar también la info del cliente
        return super().__str__() + f" - {self.num_cliente} - {self.numero_cuenta}"


# clase derivada (hereda de Persona)
class Trabajador(Persona):
    def __init__(self, nombre, apellidos, correo, num_trabajador, salario):
        # Llamamos al constructor de la clase base para inicializar los atributos heredados
        super().__init__(nombre, apellidos, correo)
        # Nuevos atributos específicos de Trabajador
        self.num_trabajador = num_trabajador
        self.salario = salario

    def __str__(self):
        # Sobrescribimos __str__ para mostrar también la info del trabajador
        return super().__str__() + f" - {self.num_trabajador} - {self.salario}"