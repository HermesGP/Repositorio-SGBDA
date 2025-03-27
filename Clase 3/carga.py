#funciones para cargar datos en una lista y para vaciarla
def llenar_lista(tamaño, tipo_de_cosas_lista = "elemento"):
    lista= []
    for i in range(tamaño):
        valor = input(f"Introduzca {tipo_de_cosas_lista} {i+1}: ")
        while (valor.isdigit() == False):
            valor = input(f"Error. Introduzca {tipo_de_cosas_lista} {i+1}: ")
        valor = int(valor)
        lista.append(valor)
    return lista
def vaciar_lista(lista):
    lista.clear()
    return lista



