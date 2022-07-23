#Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
gols = dict()
time = list()
partidas = list()
while True:
    gols.clear()
    gols['jogador'] = str(input('Nome do Jogador: '))
    jogos = int(input(f'Quantas partidas {gols["jogador"]} jogou? '))
    partidas.clear()
    for c in range(0, jogos):
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
    gols['gols'] = partidas[:]
    gols['total'] = sum(partidas)
    time.append(gols.copy())
    while True:
        cont = str(input('Quer cadastrar um novo jogador? [S/N] ')).upper()[0]
        if cont in 'SN':
            break
        print('ERRO! Responda somente S ou N')
    if cont == 'N':
        break
print('-=-' * 30)
print('cod ', end='')
for i in gols.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Qual jogador você quer ver os dados? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}!')
    else:
        print(f'   LEVANTAMENTO DO JOGADOR {time[busca] ["jogador"]}:')
        for i, g in enumerate(time[busca] ['gols']):
            print(f'     No jogo {i+1} fez {g} gols.')
        print('-' * 40)
print('<< VOLTE SEMPRE >>')






