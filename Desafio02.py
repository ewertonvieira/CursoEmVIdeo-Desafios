from datetime import date
import os
dia = input('(valor numerico (ex: 03 ou 3)Em qual dia voce nasceu: ')
mes = input('(valor numerico (ex: 12))Qual o mes: ')
ano = input('(valor numerico (ex: 01 ou 1)E em qual ano: ')
os.system('cls')
date = (dia,mes,ano)
print('Sua data de nascimento formatada(dia.mes.ano) >>', date)

