# Crie um programa onde o usuário possa digitar sete valores numéricos e
# cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.
lista = [[], []]
for c in range(1, 8):
    numeros = int(input(f'Digite o {c}o número: '))
    if numeros % 2 == 0:
        lista[0].append(numeros)
    else:
        lista[1].append(numeros)
print('-=-' * 30)
lista[0].sort()
lista[1].sort()
print(f'Os numeros pares digitados foram: {(lista[0])}')
print(f'Os números impares digitados foram: {lista[1]}')
