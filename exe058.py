# Melhore o jogo do exercicio 28 onde o computador vai 'pensar' em um número entre 0 e 10.
# Só que agora o jogador vao temtar adivimhar até acertar,
# mostrnado no final quantos palpites foram necessarios para vencer.
from time import sleep
from random import randint
computador = randint(0, 10)
print('Sou o seu computador... Acabei de pensar em um número entre 0 e 10')
print('Será que você consegue adivinha-lo? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
print('Acertou!!! Foram preciso {} tentativas...'.format(palpites))
