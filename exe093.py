#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
gols = dict()
partidas = list()
gols['jogador'] = str(input('Nome do Jogador: '))
jogos = int(input(f'Quantas partidas {gols["jogador"]} jogou? '))
for c in range(0, jogos):
    partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
gols['gols'] = partidas[:]
gols['total'] = sum(partidas)
print('-=-' * 20)
print(gols)
print('-=-' * 20)
for k, v in gols.items():
    print(f'O campo {k} tem o valor {v}')
print('-=-' * 20)
print(f'O jogador {gols["jogador"]} fez {len(partidas)} gols.')
for i, v in enumerate(gols['gols']):
    print(f'   => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {gols["total"]} gols.')
