import random
def juego_adivinar(intentos=3, numero_secreto=7):
    intentos = 3
    numero_secreto=random.choice(1, 10)
    for intentos in range(intentos):
        while True:
            numero=input(f"Intento", {intentos})
            if numero != numero_secreto:
                intentos -=1
                if intentos == 0:
                    break
                return "Has perdido todos los intentos"
            if numero == numero_secreto:
                return "Has adivinado el numero el numero era: " + numero_secreto
            break

# assert juego_adivinar() == 
# assert juego_adivinar() == 
# assert juego_adivinar() == 
#XULEI MA