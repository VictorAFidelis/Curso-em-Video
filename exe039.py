from datetime import date
print('Alistamento Militar Obrigatório!')
sexo = str(input('''Qual o seu genero? 
[ F ] Feminino
[ M ] Masculimo
'''))
if sexo in 'f' or 'F':
    print('Você não precisa realizar o alistamento!')
elif sexo in 'm' or 'M':
    print('Você precisa realizar o alistamento! ')
atual = date.today().year
nasc = int(input('Qual o ano do seu nascimento? '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIAMENTE.')
elif idade > 18:
    saldo = idade - 18
    print('Você deveria ter se alistado em {} anos.'.format(saldo))
    ano = atual- saldo
    print('Seu alistamento foi no ano de {}'.format(ano))
elif idade < 18:
    saldo = 18 - idade
    print('Você só precisa se alistar em {} anos.'. format(saldo))
    ano = atual + saldo
    print('Seu alistamento será no ano de {}.'.format(ano))
















