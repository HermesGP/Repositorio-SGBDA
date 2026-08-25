# Elije una cantidad de colores al azar de una lista
import random
colores = ["cian", "magenta", "amarillo", "rojo", "azul", "verde", "negro", "blanco"]
#con repetición
def elegir_con_repetir(lista):
    cantidad_aleatoria = random.randint(1,4)
    lista_colores_A = random.choices(lista, k=cantidad_aleatoria)
    print (lista_colores_A)
#sin repeticion
def elegir_sin_repetir(lista):
    cantidad_aleatoria = random.randint(1,4)
    lista_colores_B = random.sample(colores, k=cantidad_aleatoria)
    print (lista_colores_B)
elegir_con_repetir(colores)
elegir_sin_repetir(colores)
 
