from time import sleep
from os import system as sys
# Funcoes
def Line():
    print('___'*12)
    
def Comparar(num1, num2):
    print('Carregando resultado...')
    sleep(2)
    Line()
    if num1 > num2:
        print(f'Numero: {num1} é maior que {num2}')
    elif num2 > num1:
        print(f'Numero: {num2} é maior que {num1}')
    else:
        print(f'Numeros: {num1} e {num2} são iguais!')
    Line()
# Captura das para comparar
sys('cls')
Line()
num1 = int(input('Informe numero que deseja comparar:\n>> '))
num2 = int(input('Informe segundo numero que deseja comparar:\n>> '))
sys('cls')
Comparar(num1, num2)