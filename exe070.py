#Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
total = quantidade = menor = maior = cont = 0
barato = ''
caro = ''
while True:
    produto = str(input('Qual o nome do produto? '))
    preço = float(input('Qual o preço do produto? R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        quantidade += 1
        if cont == 1 or preço > maior:
            maior = preço
            caro = produto
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O valor da compra é R$ {total}')
print(f'{quantidade} produtos custam mais de R$ 1.000,00 reais.')
print(f'O produto mais barato custa R$ {menor:.2f} e é produto {produto}')
print(f'O produto mais caro é {caro}')

