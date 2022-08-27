#Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
valores = []
pares =  []
impares = []

while True:
    v = int(input('Digite um número: '))
    valores.append(v)
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja adicionar um novo número? [S/N] ')).strip().upper()[0]
    if 'N' == cont:
        break
print(f'Os números digitados foram {valores}')
print(f'Os números pares digitados foram {pares}')
print(f'Os números impares digitados foram {impares}')
