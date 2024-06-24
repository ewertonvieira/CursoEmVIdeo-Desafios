matriz = [[], [], []]
for line in range(0, 3):
    for col in range(0, 3):
        num = int(input(f'Digite um valor para [{line}, {col}]: '))
        matriz[line].append(num)
# Printa a matriz
print('=-='*12)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[  {matriz[l][c]}  ]', end='')
    print('')
print('=-='*12)