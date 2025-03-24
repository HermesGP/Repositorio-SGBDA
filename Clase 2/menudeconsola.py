
print(""""Menu principal, digite el número correspondiente a la operación a realizar: 
      1. Crear un nuevo registro
      2. Actualizar un registro existente
      3. Buscar entre los registros exitentes
      4. Eliminar un registro""")
while True:
    eleccion = int(input())
    match eleccion:
        case 1:
            print("Creación de Registros")
        case 2:
            print("Actualización de registros")
        case 3:
            print("Busqueda de registros")
        case 4:
            print("Eliminación de registros")
        case _:
            print("Error, favor ingresar de nuevo su elección")
            continue
    break