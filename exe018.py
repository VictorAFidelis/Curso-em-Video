# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, cos, sin, tan
an = float(input('Digite o ângulo que você deseja: '))
sen = sin(radians(an))
cos = cos(radians(an))
tan = tan(radians(an))
print(f'O angulo de {an} tem o SENO {sen:.2f} ')
print(f'O angulo de {an} tem o COSSENO de {cos:.2f}')
print(f'O angulo de {an} tem a TANGENTE de {tan:.2f}')

