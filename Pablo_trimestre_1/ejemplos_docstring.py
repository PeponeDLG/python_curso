# Docstring en Python. Buenas prácticas:

# Utiliza """ para los docstrings, según lo recomendado por PEP 8.
# Describe claramente qué hace la función, sus parámetros y lo que retorna.
# Mantén la descripción inicial breve y en mayúsculas.
# Incluye detalles sobre argumentos, valores de retorno y excepciones si son relevantes.

# Ejemplo para una función:
def mi_funcion(parametro1, parametro2):
    """
    Breve descripción de lo que hace la función en una línea.

    Esta es una descripción más detallada que explica
    el propósito y el funcionamiento de la función.

    Args:
        parametro1 (tipo): Descripción del primer parámetro.
        parametro2 (tipo): Descripción del segundo parámetro.

    Returns:
        tipo: Descripción de lo que retorna la función.

    Raises:
        TipoDeError: Explicación de cuándo se lanza esta excepción.
    """
    # Código de la función
    pass

# Ejemplo para una clase:
class Calculadora:
    """Una clase para realizar operaciones aritméticas básicas.

    Esta clase representa operaciones aritméticas que podemos llevar a cabo.
    Tiene métodos que permiten realizar las cuatro operaciones aritméticas básicas.

    Attributes:
        resultado (float): El último resultado calculado.
    """
    def __init__(self, valor_inicial=0.0):
        """Inicializa la calculadora.

        Args:
            valor_inicial (float): El valor inicial para el cálculo.
        """
        self.resultado = valor_inicial

    def sumar(self, num):
        """Suma un número al resultado actual.

        Args:
            num (float): El número a sumar.
        """
        self.resultado += num

# Acceder a la documentación. 2 maneras:
help(mi_funcion)            # Usando help()
print(mi_funcion.__doc__)   # Mostrando en consola el contenido del docstring
