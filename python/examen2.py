def nivel_peligro(cantidad):
    if cantidad == 0:
        return "Zona segura"
    elif cantidad >=1 and cantidad <=5:
        return "Peligro leve"
    elif cantidad <=9 and cantidad >=6:
        return "Peligro medio"
    else:
        return "¡Huye!"

assert nivel_peligro(0) == "Zona segura"
assert nivel_peligro(3) == "Peligro leve"
assert nivel_peligro(9) == "Peligro medio"
assert nivel_peligro(25) == "¡Huye!"

#XULEI MA