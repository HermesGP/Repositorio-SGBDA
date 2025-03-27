import dados

# un script para tirar dados y jugar a el banquero o ludo

def lanzamiento():
    resultado_dados = dados.lanzar_dados(2,6)
    print(f"Has sacado {resultado_dados}")
    movimiento = sum(resultado_dados) #suma lo que salio en los lados
    while(dados.es_doble(resultado_dados)):
        print(f"¡Has sacado doble! lanza de nuevo") #si saca los dos dados del mismo valor vuelve a tirar
        resultado_dados = dados.lanzar_dados(2,6)
        print(f"Has sacado {resultado_dados}")
        movimiento += sum(resultado_dados)
    print(f"Te mueves un total de {movimiento} casillas\n")
        


while True:
    entrada = input("Presiona enter para lanzar los dados\nTeclea \"fin\" para acabar la partida: ")
    if(entrada.lower() != "fin"):
        lanzamiento()
    else:
        break

