# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('Vamos Jogar JOKENPO!!!:')
print('''Suas Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jog = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=-' * 11)
print(f'Computador Jogou {itens[pc]}')
print(f'Jogador jogou {itens[jog]}')
print('-=-' * 11)
if pc == 0: # computador jogou PEDRA
    if jog == 0:
        print('Empatou')
    elif jog == 1:
        print('Jogador Ganhou')
    else:
        print('Computador Ganhou')
elif pc == 1: # computador jogou PAPEL
    if jog == 0:
        print('Computador Ganhou')
    elif jog == 1:
        print('Empatou')
    else:
        print('Jogador Venceu')
elif pc == 2:
    if jog == 0:
        print('Jogador Venceu')
    elif jog == 1:
        print('Computador Venceu')
    else:
        print('Empatou')


