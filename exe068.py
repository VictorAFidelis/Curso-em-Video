# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''from random import randint
print('-=-' * 10)
print('Vamos jogar PAR ou ÍMPAR')
print('-=-' * 10)
n = int(input('Diga um número: '))
pi = str(input('Par ou Ímpar? [P/I] ')).upper().strip()
pc = randint(0, 10)
result = n + pc
print(f'Você jogou {n} e o computador {pc}. Total é {result}')
if result == % 2:
    print(e é PAR')
else:
    print(f'Total deu {result} e é ÍMPAR')'''

from random import randint
v = 0
while True:
    print('-=-' * 15)
    print('JOGO DO PAR OU ÍMPAR')
    print('-=-' * 15)
    jogador = int(input('Qual o seu número? '))
    pi = str(input('Você quer Par ou Ímpar? [P/I] ')).strip().upper()[0]
    computador = randint(0, 10)
    soma = jogador + computador
    print(f'Você jogou {jogador} e o computador {computador}. O total é {soma}')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR' )
    if pi == 'P':
        if soma % 2 == 0:
            v += 1
            print('Você Venceu')
        else:
            print('Você Perdeu')
            break
    if pi == 'I':
        if soma % 2 == 1:
            print('Você Venceu')
            v += 1
        else:
            print('Você Perdeu')
            break
        print('Vamos jogar novamente...')
print(f'GAME OVER! Você ganhou {v} vezes')
