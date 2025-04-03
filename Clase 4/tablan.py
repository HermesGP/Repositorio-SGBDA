while True:
    try:
        numero = int(input('Introduce un número entero: '))
        break
    except ValueError:
        print('Error: Debes introducir un número entero.')

# Generar la tabla de multiplicar del número ingresado
nombre_archivo = f"tabla_{numero}.txt"
try:
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(f'Tabla de multiplicar del {numero}\n')
        for i in range(1, 11):
            archivo.write(f'{numero} x {i} = {numero * i}\n')
except IOError:
    print(f'Error: No se pudo escribir en el archivo {nombre_archivo}.')
else:
    print(f'Tabla de multiplicar del {numero} guardada en {nombre_archivo}.')
finally:
    print('Fin del programa.')
# Este programa genera la tabla de multiplicar de un número entero ingresado por el usuario y la guarda en un archivo de texto.

