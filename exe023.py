# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
from time import sleep
num = int(input('Digite um número: '))
u = num // 1 % 10
d = num //10 % 10
c = num //100 % 10
m = num //1000 % 10
print(f'Analisando o numero {num}')
sleep(3)
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar {m}')





