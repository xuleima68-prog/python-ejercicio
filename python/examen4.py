def leer_potencia(valor):
    try:
        potencia=int(valor)
    except ValueError:
        return "Error: la potencia debe ser un numero entero"
    return potencia

assert leer_potencia("25") == 25
assert leer_potencia("0") == 0
assert leer_potencia("abc") == "Error: la potencia debe ser un numero entero"


#XULEI MA