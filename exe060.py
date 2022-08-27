# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))''' # jeito mais simples
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
print('Calculando {} !fatorial = '.format(n), end='')
f = 1
while c > 0:
    print('{}'.format(c), end=' ')
    print('x ' if c > 1 else '= ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
