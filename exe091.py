# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
jogo = { 'Jogador 1': randint(1,6), 'Jogador 2': randint(1,6), 'Jogador 3': randint(1,6), 'Jogador 4': randint(1,6)}
ranking = list()
for k, v in jogo.items():
    sleep(1)
    print(f'{k} tirou {v} no dado.')
print('-=-' * 15)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print( '== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    sleep(1)
    print(f'{i+1} lugar: {v[0]} com {v[1]}.')




