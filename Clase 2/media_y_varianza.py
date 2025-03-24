a = [1, 4, 5, 7, 5, 9]
suma = 0
for x in a:
    suma += x
N = len(a)
media_aritmetica = suma/N
varianza = 0
for x in a:
    varianza += ((x - media_aritmetica)**2)/(N-1)
print(f"El promedio es {media_aritmetica}")
print(f"La varianza es: {varianza}")