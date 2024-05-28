from os import system
from time import sleep as slp

def Line():
    print('*_=-'*20)

def Menu(num):
    Line()
    op = int(input('Menu:\n1 - Converter para binario:\n2 - Converter para octal:\n3 - Converter para hexadecimal:\n>>> '))
    Line()
    system('cls')
    if op == 1:
        print('Convertendo numero em binario...')
        slp(2)
        print(f'O binario de {num} é {bin(num)[2:]}')
    elif op == 2:
        print('Convertendo numero em octal...')
        slp(2)
        print(f'O octal de {num} é {oct(num)[2:]}')
    elif op == 3:
        print('Convertendo numero em hexadecimal...')
        slp(2)
        print(f'O numero {num} em hexadecimal é {hex(num)[2:]}')
    else:
        print('Opcao invalida')

        
def main():
    system('cls')  
    Line()
    num = int(input('Informe numero que deseja converter\n>>> '))
    system('cls')
    Menu(num)
# Chama a funcao Main()
if __name__ == '__main__':
    main()