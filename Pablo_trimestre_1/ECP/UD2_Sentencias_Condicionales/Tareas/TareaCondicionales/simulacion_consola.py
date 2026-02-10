# Simulación de consola de comandos v1
comando = input('Introduzca el comando (Apagar/Encender): ')
if comando == 'Apagar':
    if input("¿Estás seguro? S/n ") == "S":
        print('Apagando el equipo...')
elif comando == 'Encender':
    # El único usuario del equipo es Pablo
    if input("Introduce tu nombre: ") == "Pablo":
        print('Encendemos el equipo')
    else:
        print("Usuario desconocido")
