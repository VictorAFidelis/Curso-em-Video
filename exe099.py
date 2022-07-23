# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores
# inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep

def maior(*num):
    cont = maior = 0
    print('-=' *30)
    print('Analisando os valores digitados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont +=1
    print(f'\nForam informados {cont} números e o maior é {maior}')


#programa principal
maior(5, 7, 15, 18, 25, 13)
maior(5, 9, 14, 44, 118, 358, 115, 25, 65,38, 289)


