def cargar_palabras(archivo):
    """Lee las palabras que introduce el usuario y las guarda en un archivo."""
    palabras = []
    while True:
        palabra = input("Introduce una palabra (o 'fin' para terminar): ")
        if palabra.lower() == 'fin':
            break
        palabras.append(palabra)
    try:
        with open(archivo, "a", encoding="utf-8") as archivo:
            for palabra in palabras:
                archivo.write(palabra + "\n")
    except Exception as e:
        print(f"Error al escribir en el archivo: {e}")
    else:
        print("Palabras guardadas en 'palabras.txt' correctamente.")
    finally:
        print("Fin del programa.")
def leer_palabras(archivo):
    """Lee las palabras desde un archivo y las devuelve como una lista."""
    palabras = []
    try:
        with open(archivo, "r", encoding="utf-8") as archivo:
            palabras = archivo.readlines()
        return palabras
    except FileNotFoundError:
        print(f"El archivo '{archivo}' no existe.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
cargar_palabras("palabras.txt")

palabras = leer_palabras("palabras.txt")
print("Palabras leídas del archivo:")
for palabra in palabras:
    print(palabra.strip())
