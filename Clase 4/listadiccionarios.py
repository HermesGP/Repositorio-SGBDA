contactos = [
    {"nombre": "Juan", "edad": 30, "telefono": "+595981758963"},
    {"nombre": "Maria", "edad": 25, "telefono": "+595961234567"},
    {"nombre": "Pedro", "edad": 40, "telefono": "+595992345678"},
]

# Imprimir los contactos
for contacto in contactos:
    print(contacto)
    print("-----")
for contacto in contactos:
    for llave,valor in contacto.items():
        print(f"{llave}: {valor}")
    print("-----")
    for llave in contacto.keys():
        print(f"{llave}: {contacto[llave]}")
    print("-----")
    for valor in contacto.values():
        print(f"{valor}")
    print("-----")


        
    




