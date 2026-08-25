#un script para calcular el perimetro de un polígono

from carga import *
def calcular_perimetro(lista):
    perimetro = 0
    for lado in lista:
        perimetro += lado
    print(f"El perímetro de su polígono es {perimetro}")
def preguntar_lados():
    numero_lados = int(input("Introduzca el número de lados de su poligono: "))
    lista_lados = llenar_lista(tipo_de_cosas_lista="lado", tamaño=numero_lados)
    return lista_lados

lista_lados = preguntar_lados()

perimetro = calcular_perimetro(lista_lados)

respuesta = input("Quiere calcular otro perímetro? (S/N): ")

if (respuesta.upper() == "S"):
    vaciar_lista(lista_lados)
    lista_lados = preguntar_lados()
    perimetro = calcular_perimetro(lista_lados)
    



