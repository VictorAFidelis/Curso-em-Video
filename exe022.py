# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao t odo.
# - Quantas letras tem o primeiro nome.
from time import sleep
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
sleep(3)
print(f'Seu nome em letras maiúsculas é: {nome.upper()}')
sleep(1)
print(f'Seu nome em letras minusculas é: {nome.lower()}')
sleep(1)
print(f'Seu nome tem {len(nome)} letras')
sleep(1)
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')










