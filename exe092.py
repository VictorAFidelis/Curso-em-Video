#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
# em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
cadastro = dict()
cadastro['Nome'] = str(input('Nome: '))
Nascimento = int(input('Ano de Nscimento: '))
cadastro['idade'] = datetime.now().year - Nascimento
cadastro['CTPS'] = int(input('Carteira de Trabalho (Caso não tenha, digite 0): '))
if cadastro['CTPS'] != 0:
    cadastro['Ano'] = int(input('Ano da Contratação: '))
    cadastro['Salario'] = float(input('Salário: R$ '))
    cadastro['Aposentadoria'] = cadastro['idade'] + (cadastro['Ano'] + 35) - datetime.now().year
for k, v in cadastro.items():
    print(f'{k} = {v}')
