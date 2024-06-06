lista_num = (); lista_pares = ()
for i in range(0,4):
    num = int(input("Informe um numero: "))
    lista_num = lista_num + (num, )
    if num % 2 == 0:
        lista_pares = lista_pares + (num,)
        
print("Vezes em que o 9 apareceu: ",lista_num.count(9))
print("Primeira posicao em que 3 foi digitado: ",lista_num.index(3))
print("Quais sao numeros pares: ", lista_pares)