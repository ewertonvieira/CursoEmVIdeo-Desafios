from random import randint
from time import sleep

jogadores = {}

for i in range(1, 5):
    num = randint(1, 6)
    jogadores[f'Jogador{i}'] = num
    sleep(0.5)
    print(f'O Jogador{i} tirou {jogadores[f'Jogador{i}']}')

print('Ranking dos jogadores:')
for i, item in enumerate(sorted(jogadores, key=jogadores.get, reverse=True), start = 1):
    sleep(0.5)
    print(f"{i}º lugar: {item} com {jogadores[item]}")