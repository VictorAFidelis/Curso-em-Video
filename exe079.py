# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente
valores = []
while True:
    n = (int(input('Digite um número: ')))
    if n not in valores:
        valores.append(n)
        print('Adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'A sequencia dos números digitados é {sorted(valores)}.')







