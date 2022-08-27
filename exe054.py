#Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range (1, 8):
    nasc = int(input('Em que ano a {} pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('Temos {} pessoas maiores de idade'.format(totmaior))
print('Temos {} pessoas menores de idade'.format(totmenor))




