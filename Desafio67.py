while True:
    print("-"*40)
    numero = int(input("Quer ver a tabuada de qual valor? "))
    print("-"*40)
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero  * i}")
    if numero < 0:
        print("-"*40)
        print("PROGRAMA DE TABUADA ENCERRADO. Volte sempre!")
        break