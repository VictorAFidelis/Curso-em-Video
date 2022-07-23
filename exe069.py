# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
maior = homem = mulher = 0
while True:
    idade = int(input('Qual a idade? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo? [M/F]' )).strip().upper()[0]
        if idade > 18:
            maior += 1
        if sexo == 'M':
            homem += 1
        if sexo == 'F' and idade < 20:
            mulher += 1
    parada = ' '
    while parada not in 'SN':
        parada = str(input('Deseja continuar? [S/N]' )).strip().upper()[0]
    if parada == 'N':
        break
print(f'{maior} pessoas tem mais de 18 anos.')
print(f'{homem} são homens.')
print(f'{mulher} são mulheres e tem menos de 20 anos.')

