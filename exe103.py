# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.
def ficha(jog='<desconhecido>', gol=0):
    '''
    -> Faz a amálise do nome do jogador e da quantidade de gols feitos nos campeonato.
    :param jog: Nome do Jogador
    :param gol: Número de gols feitos
    jog=<desconhecido e gol=0 - Caso o usuário não coloque algum dos dados irá retornar com esses valores.
    '''
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


# programa principal
n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)




