# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc
num = ('Digite um numero: ')
real = math.trunc(num)
print('O valor digitado foi {} e sua porção inteira é {} '.format(num, trunc))

# sem importar módulos
'''
num = float(input('Digite um numero: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, int(num)))'''
