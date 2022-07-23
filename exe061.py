#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('-=-' * 10)
print('TERMOS DE UM PA')
print('-=-' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} → '.format(cont), end='')
    termo += razão
    cont += 1
print('FIM')





