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
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')
if idade == 18:
    print('Você tem que se alistar IMEDIAMENTE.')
elif idade > 18:
    saldo = idade - 18
    print(f'Você deveria ter se alistado em {saldo} anos.')
    ano = atual- saldo
    print(f'Seu alistamento foi no ano de {ano}')
elif idade < 18:
    saldo = 18 - idade
    print(f'Você só precisa se alistar em {saldo} anos.')
    ano = atual + saldo
    print(f'Seu alistamento será no ano de {ano}.')

















