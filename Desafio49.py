from os import system
# tABUADO DE QUALQUER NUMERO INFORMADO PELO USUARIO:
def Line():
    print('_=-'*40)
system('cls')    
Line()
texto = 'TABUADA'
print(f"{texto.center(80)}")
Line()
num = int(input("INFORME UM NUMERO:"))

# Soma
for s in range(1, 11):
    print(f"{s} + {num} = {s + num}")
Line()
# Multiplicacao
for m in range(1, 11):
    print(f"{m} x {num} = {m * num}")
Line()
# Subtracao
for sb in range(1, 11):
    print(f"{sb} - {num} = {sb - num}")
Line()
# Divisao
for div in range(1, 11):
    print(f"{num} / {div} = {num / div:.1f}")
Line()