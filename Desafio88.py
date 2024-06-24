from random import sample
from time import sleep
jogos = []
# Titulo
print('*'*50)
print('MEGA SENA GERADOR'.center(48))
print('*'*50)
# Captura o numero de jogos desejado
loops = int(input('Quantos jogos voce quer que eu sorteie? '))
for k in range(0, loops):
    listjogos = sorted(sample(range(1, 60), 6))
    jogos.append(listjogos)
# Printa jogos na tela:
print('*'*15,f'SORTEANDO {loops} JOGOS','*'*16)
for p in range(1, len(jogos)+1):
    sleep(0.5)
    print(f'Jogo {p}: {jogos[p-1]}')
print('*'*17,'< BOA SORTE >','*'*18)