def calculadora_factorial():
    # Solicitamos el número al usuario
    try:
        n = int(input("Ingrese un número superior a 0 para calcular su factorial: "))
        if n <= 0:
            return "Error: El número debe ser superior a 0."
        
        # Inicializamos las variables
        factorial = 1
        contador = 1
        
        # Calculamos el factorial usando while
        while contador <= n:
            factorial *= contador
            contador += 1
            
        return f"El factorial de {n} es: {factorial}"
    except ValueError:
        return "Error: Por favor ingrese un número entero válido."

# Ejecutamos la calculadora
if __name__ == "__main__":
    resultado = calculadora_factorial()
    print(resultado)    
    