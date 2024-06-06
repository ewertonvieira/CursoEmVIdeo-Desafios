lista_num = (); lista_pares = ()
for i in range(0,4):
    num = int(input("Informe um numero: "))
    lista_num = lista_num + (num, )
    if num % 2 == 0:
        lista_pares = lista_pares + (num,)
try: 
    if lista_num.count(9) == 0:
        print("Nao temos numero 9 presente na tuplas")
    else:    
        print("Vezes em que o 9 apareceu: ",lista_num.count(9))
    print("Primeira posicao em que 3 foi digitado: ",lista_num.index(3))
    print("Quais sao numeros pares: ", lista_pares)
except ValueError:
    print("Numero 3 nao esta presente na tupla")
    print("Nao temos numeros pares na tupla")