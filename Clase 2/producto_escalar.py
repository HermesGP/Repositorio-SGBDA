a = [1, -5, 5]
b = [1, 7, -8]
suma = 0
if len(a) == len(b):
    for i in range(len(a)):
        suma += a[i]*b[i]
    print(f"El producto escalar es: {suma}")
else:
    print("Los vectores son de diferentes tamaños")