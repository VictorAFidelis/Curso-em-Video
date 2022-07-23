#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
somaidade = 0
mediaidade = 0
homemvelho = 0
nomevelho = ''
mulher = 0
for p in range(1, 5):
    print('----- {} PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        homemvelho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > homemvelho:
        homemvelho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher += 1
mediaidade = somaidade / 4
print('A soma de idade do grupo é de {} anos.'.format(mediaidade))
print('O nome do homem mais velho é {} e ele tem {} anos.'.format(nomevelho, homemvelho))
print('Ao todo {} mulheres tem menos de 20 anos'.format(mulher))








