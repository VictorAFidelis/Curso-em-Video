# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
maior = menor = 0
valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um número para a posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print(f'O maior valor digitado é {maior} e está na posição ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end=' ')
print(f'\nO menor valor digitado é {menor} e está na posição ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
