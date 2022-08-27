#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) uma contagem personalizada
from time import sleep
def linha():
    print('-=' * 20)
def contador(inicio, fim, passo):
    linha()
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if passo <0:
        passo *= -1
    if passo == 0:
        passo = 1
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            sleep(0.5)
            print(f'{cont} ', end='')
            cont += passo
        sleep(0.5)
        print('FIM')
    else:
        cont = inicio
        while cont >= fim:
            sleep(0.5)
            print(f'{cont} ', end='')
            cont -= passo
        sleep(0.5)
        print('FIM')



#Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
linha()
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
linha()
