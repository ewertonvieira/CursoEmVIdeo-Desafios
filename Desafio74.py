from random import randint

lista_num = ()
for index in range(0,4):
    num = randint(1, 10)
    lista_num = lista_num + (num,)
print("Tupla gerada: ",lista_num)
new_lista_num = tuple(sorted(lista_num))
print(f"Maior numero: {new_lista_num[3]} | Menor numero: {new_lista_num[0]}")