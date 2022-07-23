# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, cos, sin, tan
an = float(input('Digite o ângulo que você deseja: '))
sen = sin(radians(an))
cos = cos(radians(an))
tan = tan(radians(an))
print('O angulo de {} tem o SENO {:.2f} '.format(an, sen))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(an, cos))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(an, tan))
