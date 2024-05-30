from datetime import datetime
from os import system
# Instanciando ano_atual e a lista dataniver
cont = 0; cont_f = 0
ano_atual = datetime.now().year
dataaniver= [None] * 7; novadata=[None] * 7
system('cls')
print('Data de niversario(dd, mm, aa)')
for data in range(len(dataaniver)):
    dia = int(input('Informe dia: '))
    mes = int(input('Informe mes:'))
    ano = int(input('Informe ano:'))
    print('_=_'*20)
    dataaniver[data] = datetime(day=dia, month=mes, year=ano)
system('cls')
for i in range(len(dataaniver)):
    anos = ano_atual - dataaniver[i].year
    if anos>= 21:
        cont += 1
    else:
        cont_f += 1
print(f'No fim {cont_f} nao atingiram a maior idade enquanto {cont} ja atingiram.')