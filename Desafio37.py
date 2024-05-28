from time import sleep
from os import system

def line():
    print('=='*30)
# Leia numero inteiro
line()
num = int(input('Informe o numero que deseja converter:\n>>> '))
num1 = num
line()
# Escolher base de selecao
system('cls')
line()
menu = input('Menu Conversao:\n1 - Binario\n2 - Octal\n3 = Hexadecimal\n>>> ').strip()
system('cls')
line()
# selecao 1: Binario
if menu == '1':
    size = num.bit_length()
    i = 0; binary = [None] * size
    while i != size:
        binary[i] = num % 2
        num = num // 2
        i += 1
    print('Convertendo numero para Binario...')
    sleep(2)
    print(f"O numero: {num1} convertido em binario é: {' '.join(map(str, reversed(binary)))}")

# selecao 2: octal
elif menu == '2':
    print('Convertendo numero para Octal...')
    sleep(2)
    print(f'O numero: {num} convertido em Octal é: {oct(num)}')
# selecao 3: hexadecimal
elif menu == '3':
    print('Convertendo numero para Hexadecimal...')
    sleep(2)
    print(f"O numero: {num} convertido em binario é: {hex(num)}")

    