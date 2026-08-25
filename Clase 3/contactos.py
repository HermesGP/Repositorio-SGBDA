import json

contactos = [
    {"nombre": "Juan", "edad": 30, "ciudad": "Asunción"},
    {"nombre": "Ana", "edad": 25, "ciudad": "Encarnación"},
    {"nombre": "Carlos", "edad": 35, "ciudad": "Timbuctu"},
    {"nombre": "Hermenegildo", "edad": 39, "ciudad": "Madrid"}

]
#escribir en un archivo json una lista de diccionarios
def guardar_contactos(archivo):
    "Esta función carga los contactos en un archivo json"
    try:
        with open(archivo, "w") as archivo_json:
            json.dump(contactos, archivo_json, indent=4)
    except Exception as e:
        print(f"Error al cargar contactos: {e}")
    else:
        print(f"Contactos cargados en {archivo}")
    finally:
        print("Fin de la carga de contactos")
guardar_contactos("contactos.json")


def leer_contactos(archivo):
    "Esta función carga los contactos desde un archivo json en una lista de diccionarios"
    try:
        with open(archivo, "r") as archivo_json:
            contactos = json.load(archivo_json)
    except Exception as e:
        print(f"Error al cargar contactos: {e}")
    else:
        print(f"Contactos cargados desde {archivo}")
        return contactos
    finally:
        print("Fin de la carga de contactos")
contactos = leer_contactos("contactos.json")

for contacto in contactos:
    print("------------")
    for indice,valor in contacto.items():
        print(f"{indice}: {valor}")
    


