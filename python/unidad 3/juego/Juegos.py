import random  # importa random para elegir una palabra al azar
def minijuego0():
    longitud = 5  # longitud que deben tener las palabras
    intentos = 6  # numero de intentos 

    # lista de palabras para elegir la palabra secreta
    palabras = [
        "arbol", "perro", "gatos", "raton", "canto", "silla", "mesas", "jugar", "nieve", "leche",
        "fuego", "negro", "blusa", "torta", "barco", "tigre", "fresa", "pluma", "quien", "donde",
        "cabra", "lunar", "arena", "salto", "crema", "truco", "dulce", "verde", "plato", "suelo",
        "banco", "radio", "tecla", "coche", "metal", "punto", "metro", "brazo", "dedos", "cable",
        "lapiz", "tonto", "largo", "corto", "cielo", "reloj", "papas", "tapas", "canto", "grito",
        "fondo", "pasta", "panes", "torre", "campo", "mundo", "rosas", "globo", "huevo", "patas",
        "bolsa", "reina", "joven", "baile", "broma", "carne", "diosa", "lanza", "poder", "salud",
        "nacer", "coger", "beber", "andar", "saber", "oasis", "natal", "rumbo", "valor", "noble",
        "sabor", "durar", "motor", "matar", "votar", "carta", "latir", "mango", "perla", "altar",
        "ritmo", "vapor", "punto", "rival", "lanzo", "pieza", "marca", "orden", "busco", "soplo"
    ]

    palabra_secreta = random.choice(palabras)  # selecciona aleatoriamente la palabra secreta

    print("Bienvenido al falso worddle")  # mensaje de bienvenida
    print(f"Tienes {intentos} intentos para adivinar la palabra de {longitud} letras.")  # explica las reglas

    # bucle con los 6 intentos
    for intento in range(intentos):

        while True:  # el bucle es para asegurarse que el usuario escribe una palabra valida
            intento_palabra = input(f"Intento {intento + 1}: Ingresa una palabra de {longitud} letras: ").lower()  # pide una palabra

            if len(intento_palabra) == longitud and intento_palabra:  # verifica que tenga la longitud correcta
                break  # sale del bucle si ganas
            else:
                print(f"Por favor, ingresa una palabra válida de {longitud} letras.")  # mensaje de error si no das una longitud valida

        if intento_palabra == palabra_secreta:  # comprueba si la palabra es correcta
            print("¡Felicidades! Has adivinado la palabra secreta:", palabra_secreta)  # has ganado
            break  # hace break para salir del bucle si ganas

        pistas = []  # lista donde se almacenan las letras que hay en la palabra

        # generar pistas letra por letra
        for i in range(longitud):
            if intento_palabra[i] == palabra_secreta[i]:  # coincide la letra en la misma posición
                pistas.append(intento_palabra[i].upper())  # letra correcta y en la posición correcta (MAYUSCULA)

            elif intento_palabra[i] in palabra_secreta:  # la letra está en la palabra pero en otra posición
                pistas.append(intento_palabra[i].lower())  # letra correcta pero en posición incorrecta (minuscula)

            else:
                pistas.append("_")  # La letra no está en la palabra

        print("Pistas: ", " ", pistas)  # muestra las pistas de ese intento

    else:
        # si el bucle termina sin break, significa que no acertaste la palabra
        print("Lo siento, has agotado tus intentos. La palabra secreta era:", palabra_secreta) #mensaje de derrota


def minijuego1():
    preguntas = {
        "¿Cómo se imprime algo en pantalla?": "print()",
        "¿Cómo se escribe un comentario?": "#",
        "¿Cómo se suma 2 números?": "+",
        "¿Cómo se resta 2 números?": "-",
        "¿Cómo se multiplica 2 números?": "*",
        "¿Cómo se divide 2 números?": "/",
        "¿Cómo se guarda un texto en una variable?": "variable = 'texto'",
        "¿Cómo se guarda un número en una variable?": "variable = 10",
        "¿Qué función pide datos al usuario?": "input()",
        "¿Cómo se convierte un texto en número entero?": "int()",
        "¿Cómo se convierte un número en texto?": "str()",
        "¿Qué operador compara si 2 cosas son iguales?": "==",
        "¿Qué operador compara si 2 cosas son diferentes?": "!=",
        "¿Qué palabra se usa para tomar decisiones?": "if",
        "¿Cómo se empieza un bucle que se repite mientras algo sea cierto?": "while",
        "¿Cómo se empieza un bucle que recorre elementos de una lista?": "for",
        "¿Cómo se crea una lista vacía?": "[]",
        "¿Cómo se añade un elemento al final de una lista?": "append()",
        "¿Cómo se crea un diccionario vacío?": "{}",
        "¿Qué palabra devuelve un valor dentro de una función?": "return"
    }
    vidauser = 2
    puntos = 0

    # Creamos una lista de claves para acceder a las preguntas por índice
    lista_preguntas = list(preguntas.keys())

    while vidauser > 0 and puntos < 10:
        # Seleccionamos una pregunta aleatoria
        num_pregunta = random.randint(0, len(lista_preguntas)-1)
        pregunta = lista_preguntas[num_pregunta]

        # Pedimos la respuesta del usuario
        respuesta_usuario = input(pregunta + " ").lower()

        # Comprobamos la respuesta
        if preguntas[pregunta].lower() == respuesta_usuario:
            print("¡Enhorabuena! Respuesta correcta")
            puntos += 1
        else:
            print("Respuesta incorrecta, vuelve a intentarlo")
            vidauser -= 1

        print(f"Puntos: {puntos}, Vidas restantes: {vidauser}\n")

    # Mensaje final
    if puntos >= 10:
        print("¡Has ganado!")
    else:
        print("Has perdido")

def minijuego2():
    palabra=input("Escribe una palabra:")
    if len(palabra)>=6:
        print("Tu palabra es una palabra larga")
    else:
        print("tu palabra es una palabra corta")  


def minijuego3():
    cartas = ["a", "c", "c", "b", "a" ,"b"] #creo las tres opciones
    mostrar = ["_"]*6 #creo 6 cartas
    while "_" in mostrar: #mientras que hayan cartas en blanco
        print(mostrar)
        i = int(input("Carta 1: ")) #pide la carta 1
        j = int(input("Carta 2: ")) #pide la carta 2
    if cartas[i] == cartas[j]: #si las cartas coinciden
        mostrar[i] = cartas[i] 
        mostrar[j] = cartas[j]
        print("¡Match!") #lo muestra con match
    else:
        print("No coincide.") #sino no coincide
    print("¡Juego completado!")

def minijuego4 ():
    nombres = ["Gorlax", "Trunko", "Viperion"]
    niveles = [1, 2, 3]
    poderes = ["fuego", "hielo", "veneno"]
    vida = [1,2,3,4,5,6,7,8,9,10]
    print("Nombre:", random.choice(nombres))
    print("Nivel:", random.choice(niveles))
    print("Poder:", random.choice(poderes))
    print("vida:", random.choice(vida))

def minijuego5():
    pos = 4 #empiezas en la posicion 4
    while pos != 3: #mientras que la posicion sea distinto de 3
        mov = input("Mover (izq/der): ").lower() # se mueve a la izquierda o derecha
        if mov == "D": pos+=1 #si pulsas D te mueves a la derecha
        elif mov == "I" and pos > 0: pos-=1 #si pulsas I te mueves a la izquierda
        print("Posición:", pos) #te muestra la posicion
    print("¡Salida encontrada!") #has encontrado la salida

def minijuego6():
    pwd = input("Introduce contraseña: ")
    cond1 = any(c.isupper() for c in pwd) #creo la condicion de que tiene que tener una mayuscula
    cond2 = any(c.islower() for c in pwd) #creo la condicion de que tiene que tener una minuscula
    cond3 = any(c.isdigit() for c in pwd)#creo la condicion de que tiene que tener 1 digito
    cond4 = len(pwd) >= 12 #creo la condicion de que tiene que tener al menos 12 digitos
    specials= "!_#?"
    cond5 = any(c in specials for c in pwd) #creo la condicion de que tiene que tener un caracter especial
    print("Contraseña válida" if cond1 and cond2 and cond3 and cond4 and cond5 else "No válida") # la contraseña es valida solo si se cumplen todas las condiciones si no pone no valida

def minijuego7():
    jugador = cpu = 0 #los 2 jugadores empiezan con la misma puntuacion
    while jugador < 20 and cpu < 20: #mientras que los 2 jugadores tengan menos de 20 de puntuacion sigue el juego
        input("Tirar dado...") #hace un imput para tirar un dado
        jugador += random.randint(1,6) #al jugador se le suma un numero random entre 1 y 6
        cpu += random.randint(1,6) #lo mismo para el cpu
        print("Jugador:", jugador, "CPU:", cpu) #se muestran las puntuaciones
    print("¡Ganaste!" if jugador>=20 else "Perdiste.") #el primero en llegar a 20 gana

def minijuego8():
    try:
        op = input("Introduce operación: + - * /: ") #introduces un operador
        a = float(input("Introduce número 1: ")) #introduce un numero
        b = float(input("Introduce número 2: ")) #introduce el segundo numero
        match op: #hace un match case para cada operador
            case "+": 
                print(a + b)
            case "-":
                print(a - b)
            case "*":
                print(a * b)
            case "/":
                print(a / b)
            case _:
                raise ValueError #si los operadores no son correctos levanta el error value error
    except ValueError:
        print("Error: ponga un operador correcto")

def minijuego9():
    puntos = 0

    preguntas = {"¿Cuántos bits tiene un byte? ":"8","¿Qué protocolo usa la web? ":"http", "¿cuanto es 2⁸?":"256"} # hago un diccionario con 3 preguntas [clave:valor == pregunta:respuesta]
    for p, r in preguntas.items(): #pregunta respuesta en preguntas.items
        if input(p).lower() == r: #si el valor de la clave es igual a respuesta suma un punto
            puntos += 1
    print("Puntuación:", puntos, "de", len(preguntas))

def minijuego10():
    opciones = ["piedra", "papel", "tijera"] #creas 3 opciones
    vcpu=3 #creas vidas para la cpu y para el usuario
    vuser=3
    while vuser > 0 and vcpu > 0: #mientras que las vidas del user y de la cpu sean mayor que 0 se ejecuta lo siguiente
        cpu = random.choice(opciones) #la cpu elije una opcion al azar
        user = input("Elige piedra, papel o tijera: ").lower() #le dices al user que elija piedra papel o tijera
        print("CPU eligió:", cpu) 
        if user == cpu: #si han sacado lo mismo sacan empate
            print("Empate")
        elif (user == "piedra" and cpu == "tijera") or (user == "papel" and cpu == "piedra") or (user == "tijera" and cpu == "papel"): #si sacas la combinacion correcta ganas
            print("Ganaste")
            vcpu = vcpu - 1 #si ganas le bajan una vida a la cpu
        else:
            print("Perdiste") 
            vuser = vuser - 1 # si pierdes te bajan una vida
    
    print("Ganaste al mejor de 3!" if vcpu==0 else "Perdiste al mejor de 3" )

def minijuego11():
    numero_secreto = random.randint(1, 100) #genera un número aleatorio entre 1 y 100
    con=0
    while True: # repite hasta que el numero es correcto en el else y ejecyuta el break
        intento = int(input("Adivina el número (1-100): "))
        if intento < numero_secreto: # si el usuario ingresa un número menor al número secreto
            con+=1
            print("Más alto.") # indica al usuario que el número es más alto
        elif intento > numero_secreto:
            print("Más bajo.")
            con+=1
        else:
            con+=1
            print("¡Correcto!")
            break
        print(f"Has necesitado {con} intentos.")
#si se quita el int() en la línea 5, el programa lanzará un error de
# tipo porque input() devuelve una cadena y no se puede comparar directamente con un entero.

# Aquí van tus funciones minijuego1(), minijuego2(), ..., minijuego11()

def menu():
    print("""
█───█─▄▀▀─█───▄▀▀─▄▀▀▄─█▄─▄█─▄▀▀
█───█─█───█───█───█──█─█▀▄▀█─█──
█───█─█▀▀─█───█───█──█─█─▀─█─█▀▀
█▄█▄█─█───█───█───█──█─█───█─█──
─▀─▀───▀▀──▀▀──▀▀──▀▀──▀───▀──▀▀
""")
    while True:
        print(
"""
|--------------------------|
|--- MENÚ DE MINIJUEGOS ---|
|1.Juego de preguntas      |        
|2.Palabra larga o corta   |
|3.Juego de cartas         |
|4.Personaje aleatorio     |
|5.Laberinto               |
|6.Contraseña segura       |
|7.Tirar dados             |
|8.Calculadora             |
|9.Preguntas rápidas       |
|10.Piedra, papel o tijera |
|11.Adivina el número      |
|12.Falso worddle          |
|0.Salir                   |
|--------------------------|
""")
        
        opcion = input("Elige un minijuego (0-12): ")
        
        if opcion == "12":
            minijuego0()
        elif opcion == "1":
            minijuego1()
        elif opcion == "2":
            minijuego2()
        elif opcion == "3":
            minijuego3()
        elif opcion == "4":
            minijuego4()
        elif opcion == "5":
            minijuego5()
        elif opcion == "6":
            minijuego6()
        elif opcion == "7":
            minijuego7()
        elif opcion == "8":
            minijuego8()
        elif opcion == "9":
            minijuego9()
        elif opcion == "10":
            minijuego10()
        elif opcion == "11":
            minijuego11()
        elif opcion == "0":
            break
        else:
            print("Opción no válida, intenta de nuevo.")
menu()
