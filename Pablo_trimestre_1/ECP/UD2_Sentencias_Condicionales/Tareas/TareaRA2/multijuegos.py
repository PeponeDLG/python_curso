# -------------------------------------------------------------------------------------------------
# -- Pablo Chamorro Gonzalez Ripoll - Tarea de Diseño y Programación: Condicionales en Python -----
# -- 24 de noviembre de 2025 ----------------------------------------------------------------------
# 
#       ███╗░░░███╗██╗░░░██╗██╗░░████████╗██╗░░░░░██╗██╗░░░██╗███████╗░██████╗░░█████╗░░██████╗
#       ████╗░████║██║░░░██║██║░░╚══██╔══╝██║░░░░░██║██║░░░██║██╔════╝██╔════╝░██╔══██╗██╔════╝
#       ██╔████╔██║██║░░░██║██║░░░░░██║░░░██║░░░░░██║██║░░░██║█████╗░░██║░░██╗░██║░░██║╚█████╗░
#       ██║╚██╔╝██║██║░░░██║██║░░░░░██║░░░██║██╗░░██║██║░░░██║██╔══╝░░██║░░╚██╗██║░░██║░╚═══██╗
#       ██║░╚═╝░██║╚██████╔╝███████╗██║░░░██║╚█████╔╝╚██████╔╝███████╗╚██████╔╝╚█████╔╝██████╔╝
#       ╚═╝░░░░░╚═╝░╚═════╝░╚══════╝╚═╝░░░╚═╝░╚════╝░░╚═════╝░╚══════╝░╚═════╝░░╚════╝░╚═════╝░
#
# -- Idea: ----------------------------------------------------------------------------------------
# Script que ofrece un menú de tres juegos sencillos.
#
# -- Juegos incluidos: ----------------------------------------------------------------------------
# - Adivina el número
# - Piedra papel tijera
# - Juego del ahorcado
#
# -- Planteamiento inicial: -----------------------------------------------------------------------
# La idea es utilizar exclusivamente las herramientas vistas hasta ahora en la asignatura (a excep-
# ción del uso de la librerías random y os, y el uso de try/except que considero esenciales) y evi-
# tar otras metodologías más avanzadas, ya que lo que se evalúa es el uso de estructuras de control
# con condicionales y bucles, y demostrando que sólo con estas herramientas ya es posible desarro-
# llar programas completos y funcionales aplicando buenas prácticas.
# Por tanto he evitado el uso de funciones, orientación a objetos, etc. creando un script puramente
# imperativo y estructurado únicamente con condicionales y bucles 'a la antigua' aunque haya que re-
# petir algo de código.
# Nota 1: Todo el código está escrito en inglés, porque lo considero siempre una buena práctica.
# Nota 2: Todo el código está escrito a mano. No hay nada autogenerado por IA.
# 
# -- Librería random: -----------------------------------------------------------------------------
# Esta librería permite la generación pseudoaleatoria de números, esencial para crear un efecto de
# interacción del usuario con el programa.
#
# -- Librería os: ---------------------------------------------------------------------------------
# Permite interactuar con el sistema operativo. Es imprescindible para poder limpiar la consola.
# Sin ella sería muy difícil proporcionar una interfaz de texto interactiva.
# Permite la compatibilidad del script con los principales sistemas operativos: Linux, macOS y Win-
# dows.
#
# -- Uso de try/except: ---------------------------------------------------------------------------
# Cada vez que el usuario introduce información en el flujo de ejecución del programa existe la po-
# sibilidad de que se produzca una excepción. Para que ésta no interrumpa la ejecución, se captura
# permitiendo enviar un mensaje de error y continuar ejecutando el código.
# 
# -- Uso de match-case: ---------------------------------------------------------------------------
# Cuando los caminos a seguir están predefinidos, puede ser mejor usar match-case. Por ejemplo para
# el menú es recomendable, ya que las opciones a elegir están claras y el código queda más legible
# y ordenado.
# También es mejor usar match-case cuando se comparan patrones complejos, pero no es el caso en es-
# te programa, por eso no lo he usado más.
# 
# -- Uso de if/elif/else: -------------------------------------------------------------------------
# Para condiciones sencillas suele ser más recomendable usar if/elif/else en vez de match-case. Si
# las opciones pueden agruparse en rangos, como por ejemplo números comprendidos entre un valor má-
# ximo y uno mínimo, es mejor usar if/elif/else englobando las posibles opciones en vez de crear
# una estructura mucho más grande con match-case. La mayoría de las veces uso if/elif/else en éste
# código ya que creo que el resultado es más fácil de leer a simple vista.
# 
# -- Bucle principal de funcionamiento: -----------------------------------------------------------
# Una vez leídas las constantes y variables globales, el código entra en un 'bucle infinito contro-
# lado' que corresponde con la ejecución del menú de opciones con los distintos juegos. La única ma-
# nera de salir de este bucle principal es eligiendo la opción correspondiente para salir del pro-
# grama. Mientras tanto, se puede jugar ininterrumpidamente a los juegos.
# 
# -- Menú de opciones: ----------------------------------------------------------------------------
# El menú de opciones es una estructura match-case con 5 opciones: una para cada juego, una para
# salir del programa y una última por defecto para gestionar la entrada de datos incorrecta.
# 
# -- Adivina el número: ---------------------------------------------------------------------------
# Se genera aleatoriamente un número del 1 al 10, y el usuario tiene que adivinarlo. Tiene 3 inten-
# tos y si no lo adivina se muestra como pista si el número correcto es mayor o menor.
# 
# -- Piedra papel tijera: -------------------------------------------------------------------------
# Se genera aleatoriamente la jugada de la máquina, que puede ser piedra (gana tijera), papel (gana
# a piedra) o tijera (gana a papel). Luego se recoge la jugada del usuario y se genera el resulta-
# do.
# 
# -- Juego del ahorcado: --------------------------------------------------------------------------
# Se elige aleatoriamente una palabra de una lista de palabras y se muestran tantas barras bajas
# ('_') como letras contenga. Se va pidiendo al jugador que introduzca una letra y si está en la
# palabra, se va rellenando. Si falla, se resta uno de un total de 5 intentos.
#
# Nota: No he incluido ejemplos de prueba porque como el programa es totalmente interactivo no los
# considero necesario
# 
# -- Fuentes de ayuda externas: -------------------------------------------------------------------
# Web usada para generar los gráficos Unicode: https://fsymbols.com/es/generadores/
# Documentación de uso de la librería random: https://docs.python.org/es/3.10/library/random.html
# Documentación de uso de la librería os: https://docs.python.org/es/3.10/library/os.html
# -------------------------------------------------------------------------------------------------

# Importa las librerías externas
import random, os

# Variables y constantes globales
INTRO = '''
    ███╗░░░███╗██╗░░░██╗██╗░░████████╗██╗░░░░░██╗██╗░░░██╗███████╗░██████╗░░█████╗░░██████╗
    ████╗░████║██║░░░██║██║░░╚══██╔══╝██║░░░░░██║██║░░░██║██╔════╝██╔════╝░██╔══██╗██╔════╝
    ██╔████╔██║██║░░░██║██║░░░░░██║░░░██║░░░░░██║██║░░░██║█████╗░░██║░░██╗░██║░░██║╚█████╗░
    ██║╚██╔╝██║██║░░░██║██║░░░░░██║░░░██║██╗░░██║██║░░░██║██╔══╝░░██║░░╚██╗██║░░██║░╚═══██╗
    ██║░╚═╝░██║╚██████╔╝███████╗██║░░░██║╚█████╔╝╚██████╔╝███████╗╚██████╔╝╚█████╔╝██████╔╝
    ╚═╝░░░░░╚═╝░╚═════╝░╚══════╝╚═╝░░░╚═╝░╚════╝░░╚═════╝░╚══════╝░╚═════╝░░╚════╝░╚═════╝░
'''
OPTIONS_MENU = '''
    -- Menú de opciones --

    Escribe el número correspondiente:
    1 - Adivina el número
    2 - Piedra papel tijera
    3 - Juego del ahorcado
    0 - Salir
'''
GUESS_THE_NUMBER = '''
    ▄▀█ █▀▄ █ █░█ █ █▄░█ ▄▀█   █▀▀ █░░   █▄░█ █░█ █▀▄▀█ █▀▀ █▀█ █▀█
    █▀█ █▄▀ █ ▀▄▀ █ █░▀█ █▀█   ██▄ █▄▄   █░▀█ █▄█ █░▀░█ ██▄ █▀▄ █▄█

    Adivina un número del 1 al 10. ¡Tienes 3 intentos!
'''
ROCK_PAPER_SCISSORS = '''
    █▀█ █ █▀▀ █▀▄ █▀█ ▄▀█   █▀█ ▄▀█ █▀█ █▀▀ █░░   ▀█▀ █ ░░█ █▀▀ █▀█ ▄▀█
    █▀▀ █ ██▄ █▄▀ █▀▄ █▀█   █▀▀ █▀█ █▀▀ ██▄ █▄▄   ░█░ █ █▄█ ██▄ █▀▄ █▀█

    Elige piedra papel o tijera.
    Piedra rompe a tijera. Papel envuelve a piedra. Tijera corta a papel.
'''
HANGMAN_GAME = '''
    ░░█ █░█ █▀▀ █▀▀ █▀█   █▀▄ █▀▀ █░░   ▄▀█ █░█ █▀█ █▀█ █▀▀ ▄▀█ █▀▄ █▀█
    █▄█ █▄█ ██▄ █▄█ █▄█   █▄▀ ██▄ █▄▄   █▀█ █▀█ █▄█ █▀▄ █▄▄ █▀█ █▄▀ █▄█

    Adivina la palabra. ¡Tienes 5 intentos!
'''
YOU_WIN = '''
    ▀ █░█ ▄▀█ █▀   █▀▀ ▄▀█ █▄░█ ▄▀█ █▀▄ █▀█ █
    █ █▀█ █▀█ ▄█   █▄█ █▀█ █░▀█ █▀█ █▄▀ █▄█ ▄
'''
YOU_LOSE = '''
    
    █░█ ▄▀█ █▀   █▀█ █▀▀ █▀█ █▀▄ █ █▀▄ █▀█
    █▀█ █▀█ ▄█   █▀▀ ██▄ █▀▄ █▄▀ █ █▄▀ █▄█
'''
DRAW = '''
    █▀▀ █▀▄▀█ █▀█ ▄▀█ ▀█▀ █▀▀
    ██▄ █░▀░█ █▀▀ █▀█ ░█░ ██▄
'''
OUTRO = ''' 
█▀ ▄▀█ █░░ █ █▀▀ █▄░█ █▀▄ █▀█   █▀▄ █▀▀ █░░   ░░█ █░█ █▀▀ █▀▀ █▀█   ░   ░   ░
▄█ █▀█ █▄▄ █ ██▄ █░▀█ █▄▀ █▄█   █▄▀ ██▄ █▄▄   █▄█ █▄█ ██▄ █▄█ █▄█   ▄   ▄   ▄
'''
ROCK_PAPER_SCISSORS_LIST = ["piedra", "papel", "tijera"]
WORDS_LIST = ["bloque", "bucle", "código", "condicional", "control", "diagrama", "estructura", "flujo", "problema", "programa", "python", "variable"]
system = os.name # Identifica el sistema operativo

print(INTRO)

# Bucle principal
while True:
    # Menú de opciones
    print(OPTIONS_MENU)

    # Captura la posibilidad de que el usuario no introduzca un número
    try:
        option = int(input("Elige una opción: "))
    except ValueError:
        print("Error: Introduce un número.")
        continue

    # Limpia la consola
    if system == "posix":
        os.system('clear') # Para Linux y macOS
    else:
        os.system('cls') # Para Windows
    
    match option:
        case 1: # Juego de adivinar un número
            print(GUESS_THE_NUMBER)
            random_number = random.randint(1, 10) # Genera un número aleatorio del 1 al 10
            for i in range(1, 4): # Bucle con 3 intentos
                # Captura la posibilidad de que el usuario no introduzca un número
                try:
                    user_number = int(input(f"Intento {i}: "))
                except ValueError:
                    print("Error: Introduce un número.")
                    continue

                if user_number == random_number:
                    print(f"¡Has acertado en el {i}º intento!")
                    print(YOU_WIN)
                    break
                elif user_number < random_number:
                    print("Has fallado. El número es mayor.")
                else:
                    print("Has fallado. El número es menor")
            else:
                print(YOU_LOSE)

        case 2: # Piedra papel tijera
            print(ROCK_PAPER_SCISSORS)
            random_move = ROCK_PAPER_SCISSORS_LIST[random.randint(0, 2)] # Jugada aleatoria
            user_move = input("Escribe tu jugada: ").lower() # Pasa a minúsculas por si acaso
            print(f"{user_move} vs {random_move} . . .") # Muestra la jugada
            # Comprueba que el usuario haya introducido una opción correcta
            if user_move in ROCK_PAPER_SCISSORS:
                if user_move == random_move:
                    print(DRAW)
                elif user_move == "piedra" and random_move == "tijera":
                    print(YOU_WIN)
                elif user_move == "papel" and random_move == "piedra":
                    print(YOU_WIN)
                elif user_move == "tijera" and random_move == "papel":
                    print(YOU_WIN)
                else:
                    print(YOU_LOSE)
            else:
                print("No he entendido tu jugada.")
                print("Saliendo del juego . . .")

        case 3: # Juego del ahorcado
            print(HANGMAN_GAME)
            random_word = WORDS_LIST[random.randint(0, len(WORDS_LIST) - 1)] # Palabra al azar
            hidden_word = "" # Plantilla vacía para la palabra oculta
            chars = [] # Lista de caracteres elegidos por el usuario
            lives = 5 # Intentos restantes

            while lives > 0: # Bucle del juego
                # Captura la posibilidad de que el usuario no introduzca un carácter
                try:
                    user_char = input("Escribe una letra: ").lower() # Pasa a minúsculas
                except ValueError:
                    print("Error: Introduce una letra.")
                    continue
                
                chars.append(user_char) # Guarda cada letra elegida por el usuario

                # Construye la palabra con las letras elegidas y los espacios restantes
                for char in random_word:
                    if char in chars:
                        hidden_word += char
                    else:
                        hidden_word += "_"
                print(hidden_word) # Muestra la palabra parcialmente descubierta
                
                # Comprueba si en este turno se ha acertado o no
                if user_char in random_word:
                    print("Letra encontrada.")
                    if hidden_word == random_word: # Comprueba si la palabra ha sido completada
                        print(YOU_WIN)
                        break
                else:
                    lives -= 1
                    print(f"Has fallado. Vidas restantes: {lives}")
                    if lives == 0: # Comprueba si quedan intentos
                        print(YOU_LOSE)
                        break 
                hidden_word = "" # Reinicia la palabra oculta

        case 0: # Sale del bucle principal
            print(OUTRO)
            break

        case _: # Opción incorrecta
            print("Opción incorrecta.")
