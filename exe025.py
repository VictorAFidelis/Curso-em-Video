# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite seu nome competo:')).strip()
print('Seu nome tem Silva? {}'.format('Silva' in nome.upper()))

