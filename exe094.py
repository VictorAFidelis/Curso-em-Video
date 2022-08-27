#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
# em um dicionário e todos os dicionários em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média
galera = list()
dados = dict()
soma = média = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Qual o nome da pessoa? '))
    while True:
        dados['sexo'] = str(input('Qual o sexo [M/F]? ')).upper().strip()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO1. Por favor digite somente M ou F.')
    dados['idade'] = int(input('Digite a idade da pessoa: '))
    soma += dados['idade']
    galera.append(dados.copy())
    while True:
        cont = str(input('Deeja realizar um novo cadastro[S/N]? ')).upper().strip()[0]
        if cont in 'SN':
            break
        print('ERRO!. Digite somente S ou N.')
    if cont == 'N':
        break
print('-=-' * 30)
print(galera)
print(f'Foram cadastradas {len(galera)} pessoas')
média = soma / len(galera)
print(f'A média de idade das pessoas cadastradas é {média:5.2f}')
for p in galera:
    if p["sexo"] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
for p in galera:
    if p['idade'] >= média:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO  >>')
