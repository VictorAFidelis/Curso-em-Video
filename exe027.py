# aça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite seu nome completo:')).strip()
dividido = nome.split()
print(f'Seu primeiro nome é {dividido[0]}')
print(f'Seu último nome é {dividido[len(dividido)-1]}')







