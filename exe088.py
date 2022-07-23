# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.
# Realizar um loop infinito onde vamos inserir os numeros na lista.
from random import randint
from time import sleep
lista = list() # lista inicial dos jogos
jogos = list() # lista final onde será copiado os jogos
print('-' * 30)
print('     JOGA NA MEGA SENA     ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1 # para somar a quantidade de jogos a criar
while tot <= quant: # enquanto o total for menor que a quantidade de jogos
    cont = 0 # para contar quantos números devem ser sorteados
    while True:
        n = randint(1, 60) # gerar numeros entre 1 e 60
        if n not in lista: # Se o número não estiver na lista
            lista.append(n) # inserir o número na lista
            cont += 1 # contagem de quantos números já foram inseridos na lista
        if cont >= 6: # Se a quantidade de números na lista for maior ou igual a 6
            break # parar a inserção de novo números
    lista.sort() # para organizar em ordem a lista
    jogos.append(lista[:]) # copiando os dados da lista para a jogos
    lista.clear() # limpa a lista para não exibir duplicado
    tot += 1
print(f'-=-' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)
for i, l in enumerate(jogos): # Para cada indice na lista de jogos, enumere o jogo
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=-' * 4, 'BOA SORTE', '-=-' * 4)



