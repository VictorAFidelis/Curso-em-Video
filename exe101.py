#Crie um programa que tenha uma função chamada voto() que vai
#receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor
# literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO
# nas eleições.
def voto(nasc):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - nasc
    if idade <= 15:
        return f'Sua idade é {idade}. Voto Negado'
    elif 16 <= idade < 18:
        return f'Sua idade é {idade}. Voto OPCIONAL'
    elif idade >= 65:
        return f'Sua idade é {idade}, seu voto é OPCIONAL'
    else:
        return f'Sua idade é {idade}. Seu voto é OBRIGATÓRIO'


# Programa Principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
