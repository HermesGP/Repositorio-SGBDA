palabra = input("Introduce una palabra: ")
palabra.lower()
vocales = ['a', 'e', 'i', 'o', 'u']
for vocal in vocales: 
    veces_que_aparece = 0
    for letter in palabra: 
        if letter == vocal:
            veces_que_aparece += 1
    print(f"La vocal {vocal} aparece {veces_que_aparece} veces")
        


