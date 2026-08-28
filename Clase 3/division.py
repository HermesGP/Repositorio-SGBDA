
def dividir():
    "Divide dos numeros proveidos por el usuario y devuelve el resultado"
    while True:
        try:
            numerador = float(input("Introduce el numerador: "))
            denominador = float(input("Introduce el denominador: "))
            division = numerador / denominador
        except ValueError:
            print("Por favor, introduce solo numeros.")
            continue
        except ZeroDivisionError:
            print("El denominador no puede ser cero.")
            continue
        else:
            return division
        finally:
            print("Intento de division realizado.")

division =dividir()
print(f"El resultado de la division es: {division}")
# Este script define una funcion que permite dividir dos numeros introducidos por el usuario.





        
    




