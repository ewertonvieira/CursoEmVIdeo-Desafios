num = []
numimpares = []
numpares = []
while True:
    number = int(input('Digite um nuemro: '))
    num.append(number)
    op = input('Deseja continuar?..[S para fim da execução]: ').upper().strip()
    if op in ['S']:
        break
for i in num:
    if i % 2 == 0:
        numpares.append(i)
    else:
        numimpares.append(i)
print(f'Lista completa: {num}')
print(f'Lista de numeros pares: {numpares}')
print(f'Lista de numeros impares: {numimpares}')