#Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = dict()
aluno['Nome'] = str(input('Nome do Aluno: '))
aluno['Média'] = float(input(f'Média do {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Em Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
# print(f"O {aluno['Nome']} tem a média {aluno['Média']}.\nSua situação é {aluno['Situação']}")
""" Guanabara traz a seguinte solução para o final"""
for k, v in aluno.items():
    print(f'  - {k} é igual {v}')
