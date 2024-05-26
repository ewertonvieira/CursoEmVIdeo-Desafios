from random import randint
print('Pensando em um numero entre 0 e 5....') 
number = randint(0, 5)
print(number)
numuser = int(input('Qual numero voce acha que foi? '))
if numuser == number:
    print(f'Voce acertou! O numero que pensei foi {numuser}!')
else:
    print(f'Infelizmente voce errou! O numero que pensei foi {number} e nao {numuser}...')
