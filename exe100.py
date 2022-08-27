# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
# a soma entre todos os valores pares sorteados pela função anterior.
import random
from time import sleep
def sortear(lista):
    print('Sorteando 5 valores da lista... ', end='')
    for cont in range(1, 6):
        n = random.randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.5)

def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'\nSomando os valores pares da {lista} temos {soma}')


numeros = list()
sortear(numeros)
somapar(numeros)
