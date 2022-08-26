#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[033m', end='')
        tot += 1
    else:
        print('\033[031m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} é divisivel {} vezes.'.format(n, tot))
if tot == 2:
    print('E por isso ele é PRIMO')
else:
    print('Por isso ele NÃO É PRIMO')







