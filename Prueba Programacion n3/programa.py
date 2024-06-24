
# Importar Json y convertir a diccionario python

import json
from funciones import *

with open("biblioteca.json", "r", encoding="utf8") as biblioteca:
    read = biblioteca.read()
dic_biblioteca = json.loads(read)


# Menu principal

print("[1] - Mantenedor de libros")
print("[2] - Reportes")
print("[3] - Salir")

selection = str(input("Ingrese opcion: "))
while True:
    if selection == "1":
        print("[1] - Agregar libro")
        print("[2] - Editar libro")
        print("[3] - Eliminar libro")
        print("[4] - Buscar libro")
        print("[5] - volver")
        selection = str(input("Ingrese opcion: "))
        while True:
            if selection == "1":
                nombre_libro = str(input("Titulo de libro a agregar: "))
                agregar_libro(nombre_libro, dic_biblioteca)
                selection = str(input("Ingrese opcion: "))
                with open("biblioteca.json", "w", encoding="utf8") as biblio:
                    esrcibir = json.dumps(dic_biblioteca)
                    biblio.write(esrcibir)

            if selection == "2":
                libro_id = int(input("Ingrese LibroID: "))
                modificar_libro(libro_id, dic_biblioteca)
                selection = str(input("Ingrese opcion: "))

        

