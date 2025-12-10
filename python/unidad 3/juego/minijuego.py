import random  # importa random para elegir una palabra al azar

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
