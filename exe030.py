#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
n = int(input('Diga um número: '))
resul = n % 2
if resul == 0:
    print(f'O número {n} é PAR')
else:
    print(f'O número {n} é IMPAR')

