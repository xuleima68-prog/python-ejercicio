biblioteca_musical = []

# Ejercicio 1: Función para agregar canciones
def agregar_cancion(titulo, artista, año):
    # Pista: crea una tupla y añádela a la lista biblioteca_musical
    cancion_tupla=(titulo,artista,año)
    biblioteca_musical.append(cancion_tupla)

# Test
agregar_cancion("Hotel California", "Eagles", 1977)
agregar_cancion('Bohemian Rhapsody','Queen',1975)
agregar_cancion('Imagine','John Lennon',1971)
assert isinstance(biblioteca_musical[0], tuple), 'Cada canción debe ser una tupla'
assert len(biblioteca_musical)==3, 'Debe haber 2 canciones en la lista'

# Ejercicio 2: Función para mostrar canciones
def mostrar_canciones(orden='titulo'):
    # Pista: ordena la lista según el parámetro 'orden' y luego imprime cada canción 
    if orden == 'titulo':
        canciones_ordenadas = sorted(biblioteca_musical, key=lambda x: x[0])
    elif orden == 'artista':
        canciones_ordenadas = sorted(biblioteca_musical, key=lambda x:x[1])
    for cancion in canciones_ordenadas:
        print(f"el titulo es {cancion[0]} y el artista es {cancion[1]}")
mostrar_canciones()


# Ejercicio 3: Función para buscar canciones por palabra clave en el título
def buscar_cancion(palabra):
    # Pista: recorrer biblioteca_musical, usar .lower() y comprobar si la palabra está en el título
    i=0
    resultado = []
    for cancion in biblioteca_musical:
        if palabra.lower() in cancion[0].lower():
            print(f"tu palabra si esta en titulo y esta en la cancion {biblioteca_musical[i]}")
            resultado.append(biblioteca_musical[i])
        i+=1
    return resultado


# Test
resultado = buscar_cancion('imagine')
assert all('imagine' in t[0].lower() for t in resultado), 'Todos los títulos deben contener la palabra'



# Ejercicio 4: Función para estadísticas por artista
def estadisticas():
    # Pista: crear diccionario, recorrer biblioteca_musical y contar canciones por artista
    mi_diccionario = {}
    for cancion in biblioteca_musical:
        artista = cancion [1]
        if artista not in mi_diccionario:
            mi_diccionario[artista] = 1
        else:
            mi_diccionario[artista] +=1
    return mi_diccionario


# Test
stats = estadisticas()
assert isinstance(stats, dict), 'Debe devolver un diccionario'
assert stats.get('Queen',0)>=1, 'Queen debe aparecer en las estadísticas'









def main():
    agregar_cancion()
    mostrar_canciones()
    buscar_cancion()
    estadisticas()
