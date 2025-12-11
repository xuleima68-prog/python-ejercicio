def calcular_energia_final(energia_base, factor):
    FACTOR_MINIMO = 0.1
    energia_base = int(energia_base)
    if factor < FACTOR_MINIMO: #si factor es menor que FACTOR_MINIMO
        factor = float(factor) #convertir el int de factor a float
        factor == FACTOR_MINIMO #cambia el valor de factor por FACTOR_MINIMO
    energia_final = energia_base * factor
    return energia_final

assert calcular_energia_final(100, 0.5) == 50.0
assert calcular_energia_final(100, 0.01) == 1.0 #te lo pongo aqui la manera que deberia de ser correcta que 100*0.01 da 1 y no 10
assert calcular_energia_final(100, 0.01) == 10.0 #profe 100 * 0.01 el resultado es 1 no 10 por lo que aqui va a dar error y no se va a poder hacer
assert calcular_energia_final(0, 0.5) == 0

#XULEI MA