#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.
''' Forma matemática:
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = (co **2 + ca **2) ** (1/2)
print('O valor da hipotenusa é {}'.format(hi)) '''
import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = math.hypot(ca, co)
print(f'O valor da hipotenusa é {hi:.2f}')


