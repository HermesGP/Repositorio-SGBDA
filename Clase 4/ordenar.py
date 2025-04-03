# Este programa lee un archivo de texto llamado "palabras.txt", ordena las palabras alfabéticamente y las guarda en otro archivo llamado "ordenadas.txt".
try:   
    with open("palabras.txt", "r", encoding="utf-8") as archivo:
        lista_palabras = archivo.readlines()
except FileNotFoundError:
    print("El archivo 'palabras.txt' no fue encontrado.")
except Exception as e:
    print(f"Error inesperado al leer el archivo: {e}")
else:
    lista_palabras.sort()
    # Eliminar espacios en blanco al inicio y al final de cada palabra
    # y eliminar saltos de línea
for palabra in lista_palabras:
    palabra = palabra.strip()
try:
    with open("ordenadas.txt", "w", encoding="utf-8") as archivo:
        archivo.writelines(lista_palabras)
except PermissionError:
    print("No se tienen permisos para escribir en 'ordenadas.txt'.")
except Exception as e:
    print(f"Error inesperado al escribir el archivo: {e}")
