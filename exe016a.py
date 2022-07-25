# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc
num = ('Digite um numero: ')
real = math.trunc(num)
print(f'O valor digitado foi {num} e sua porção inteira é {trunc} ')
# sem importar módulos
num = float(input('Digite um numero: '))
print(f'O valor digitado foi {num} e sua porção inteira é {int(num)}')

