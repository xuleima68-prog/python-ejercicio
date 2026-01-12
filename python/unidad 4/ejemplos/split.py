#notas
#alumno; ap_web; seg; python
#pepe 7; 8; 9;
#juanito 6; 7; 8;

whitespace_line = "alumno ap_web seg python"
cols = whitespace_line.split()
print("Estas son las columnas separadas por un espacio en blanco", cols)

text_line = "pepe; 7; 8; 9;"
cols = text_line.split("; ")
alumno = cols[0]
notas = cols[1:4]
print("El alumno es:", alumno)
print("Las notas son:", notas)

cadena = "    hola mundo    ".strip()
print("Quita todos los espacios del final y del principio:", cadena)

tupla = (1, 2, 3)
lista_tupla = list(tupla)#guarda la tupla como lista
lista = [1, 2, 3]
print("una tupla no puede ser editada", type(tupla))
print("una lista puede ser editada", type(lista))

carton_bingo = [
    [1, 2, 3, 4, 5], #fila 0
    [6, 7, 8, 9, 10], #fila 1
    [11, 12, 13, 14, 15] #fila 2
]
# Mostrar el id (índice) y la fila usando enumerate (id 0-based)
for idx, fila in enumerate(carton_bingo):
    print(f"Fila id: {idx} -> {fila}")
    for numero in fila:
        print(f"Numero del bingo (fila {idx}): {numero}")

colores = ["rojo", "verde", "azul"]
borrar=colores.pop(2)
colores.remove(borrar)
print(colores)



# --------------------tuplas------------------
titulo = "Titulo 1"
tupla_libro = (titulo, 2000, "Tolkein")
print("tupla_libro acceder a año", tupla_libro[1])
print("Tupla antes de cambair el titulo", tupla_libro)

titulo = "Titulo 2"
print("Tupla despues de cambiar el libro", tupla_libro)

mysql_conn_params = ("http://phpmyadmin", 336, "root")

url, port, user = mysql_conn_params

urñ, *others = mysql_conn_params

print(others)

libros = [("libro 1", 2000, "Tolkein"), ("libro2", 2020, "Tolkein 2")]
for titulo, year, author in libros:
    print(year)

"""
libros = [("libro 1", 2000, "Tolkein"), ("libro2", 2020, "Tolkein 2")]
for libro in libros:
    print(libros)
"""