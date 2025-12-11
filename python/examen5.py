def calcular_puntos(velocidad, choques):
    puntos = velocidad * 2 - choques * 3
    if puntos < 0:
        return 0
    else:
        return puntos

assert calcular_puntos(10, 2) == 14
assert calcular_puntos(5, 10) == 0
assert calcular_puntos(0, 0) == 0



#XULEI MA