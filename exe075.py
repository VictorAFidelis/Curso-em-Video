#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

numeros = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')),
           int(input('Digite um número: ')))
print(f'Você digitou os números {numeros}')
print(f'O número 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O numero 3 apareceu na posição {numeros.index(3)+1}')
else:
    print('O número 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados são:', end=' ')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')





