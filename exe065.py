# Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
resp = 'S'
soma= 0
quant = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    resp = str(input('Quer continuar:? [S/N] ')).upper().strip()[0]
    quant += 1
    soma += num
print('Você digitou {} números. A soma dos valores digitados é {}.'.format(quant, soma))
media = soma / quant
print('A média dos valores digitados é {}'.format(media))
print('Acabou')
