# Importamos la clase Coche desde el archivo coche.py
from coche import Coche

# Creamos distintos objetos de la clase Coche con valores personalizados
coche1 = Coche("Amarillo", "Ferrari", "Aventador", 300, 500, 2)

print(coche1.color) # Acceso a un atributo público
print(coche1._velocidad) # Acceso a un atributo protegido

# Acceso a un atributo privado. Se produce un error, no se puede acceder a un atributo privado desde fuera de la clase
# print(coche1.__marca) 
  
# print(coche1.getInfo()," - ",coche1.__atributoPrivado)
Coche.estatico("hola")

coche1.meloinvento = "Atributo inventado"
print(coche1.meloinvento)