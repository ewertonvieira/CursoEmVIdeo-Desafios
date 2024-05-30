from time import time
init = time()
#
peso = [float] * 5
for k in range(len(peso)):
    peso[k] = float(input('Informe peso: '))
# Organiza do maior para o menor
print(f'Maior: {max(peso)}\nMenor: {min(peso)}')
end = time()
print(f'{end - init:.2f}s')
