from time import sleep
from os import system

for i in range(10, -1, -1):
    print("-"*4,"Contagem-Regressiva","-"*4)
    print('>'*12,f'{i}s','<'*12)
    sleep(1)
    system('cls')