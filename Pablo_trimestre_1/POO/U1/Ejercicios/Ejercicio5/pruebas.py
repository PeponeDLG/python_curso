from clase_coche import Coche

# Crea varias instancias
coche_1 = Coche("Audi", "Q2", 2008, 234123)
coche_2 = Coche("Ford", "Focus", 2003, 485768)
coche_3 = Coche("Ferrari", "Testarossa", 1985, 102934)
coche_4 = Coche("Audi", "Q2", 2008, 234123)

# Prueba los métodos
print(coche_1.get_info())
print("-"*100)
print(coche_2.get_instance_values())
print("-"*100)
print(coche_1.__eq__(coche_2))
print(coche_1.__eq__(coche_4))
print("-"*100)
coche_4.remove_instance()
