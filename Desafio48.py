# Soma de todos os numeros multiplos de 3 entre 1 e 500:
soma = 0;
print("_-"*38, 'MULTIPLOS-DE-3-E-IMPARES', "_-"*38)
print('Lista: ')
for i in range(1, 501):
    if i % 2 != 0:
        if i % 3 == 0:
            print(f'{i}', end = ' ')
            soma  += i
print(f'\nA soma deles: {soma}')