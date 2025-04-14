from math import gcd
class fracción:
    def __init__(self, numerador, denominador):
        # raise sirve para llamar a una excepción, en este caso ZeroDivisionError
        if denominador == 0:
            raise ZeroDivisionError("El denominador no puede ser cero.")
        else:
            # Asegurar que el signo negativo esté en el numerador
            if denominador < 0:
                numerador = -numerador
                denominador = -denominador
            self.numerador = numerador
            self.denominador = denominador

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def simplificar(self):
        # Calcular el MCD del numerador y el denominador
        # y dividir ambos por el MCD para simplificar la fracción
        divisor = gcd(self.numerador, self.denominador)
        return fracción(self.numerador // divisor, self.denominador // divisor)

    def suma(fraccion1, fraccion2):
        nuevo_numerador = (fraccion1.numerador * fraccion2.denominador) + (fraccion2.numerador * fraccion1.denominador)
        nuevo_denominador = fraccion1.denominador * fraccion2.denominador
        return fracción.simplificar(fracción(nuevo_numerador, nuevo_denominador))

fraccion1 = fracción(1, 2)
fraccion2 = fracción(3, 4)
suma = fracción.suma(fraccion1, fraccion2)
print(f"Suma: {suma}")

