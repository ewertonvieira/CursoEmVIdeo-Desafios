import pygame as pg
# Saida de texto, nada de mais; 
print('Play Music: "bullfight_a_day_to_remember.mp3"')
# Inicia todos o mudulos de pygame;
pg.init()
# Carregando aquivo de audio | Pasta raiz referente ao Desafio21.py
pg.mixer.music.load('mp3/bullfight_a_day_to_remember.mp3')
# Inicia a reproducao;
pg.mixer.music.play()
# Aguando entrada(Enter) do usuario, impedidndo fim da execucao antes da hora. 
input()