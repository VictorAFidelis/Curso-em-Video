# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
dado = []
pessoas = []
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    resp = str(input('Quer Continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=-' * 30)
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso digitado foi {maior}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso digitado foi {menor}kg. Peso de ',end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]} ', end='')
print()




