from random import randint as lanzar

def lanzar_dados(cantidad, tamaño):
    resultados = []
    for _ in range(cantidad):
        resultado = lanzar(1,tamaño)
        resultados.append(resultado)
    return resultados

def es_doble(lista):
    doble = (lista[0] == lista[1])
    return doble