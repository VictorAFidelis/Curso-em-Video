# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math

num = float(input('Digite um numero: '))
real = math.trunc(num)
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, math.trunc(num)))

