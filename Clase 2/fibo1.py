# lista inicial para evitar error de fuera del rango
lista_fibo = [0, 1]
while True:
    entrada = input("Por favor, introduce la longitud de tu secuencia: ")
    if entrada.isdigit():
        numero = int(entrada)
        # debe ser una lista de al menos 3 numeros
        if numero >= 3:  
            break
        else:
            print("Eso no es un número válido. Inténtalo de nuevo.")  
    else:
        print("Eso no es un número válido. Inténtalo de nuevo.")
for i in range(2,numero):
    lista_fibo.append(lista_fibo[i - 1] + lista_fibo[i - 2])

print("Secuencia de fibonacci: ")
print(lista_fibo)

        


