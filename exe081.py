# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
valores = []
while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    valores.sort(reverse=True)
    cont = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
print(f'Foram digitados {len(valores)} números')
print(f'Os números digitados em ordem decrescente foram {valores}')
if 5 in valores:
    print('O número 5 está na lista!')
else:
    print('O número 5 não está na lista!')
