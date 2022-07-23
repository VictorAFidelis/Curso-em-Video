#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ('Palmeiras', 'Flamengo', 'Internacional', 'Gremio', 'São Paulo', 'Atlético Mineiro', 'Athletico', 'Cruzeiro', 'Botafogo',
         'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará', 'Vasco', 'América', 'Sport', 'Vitória', 'Paraná')
# for cont in range(0, len(times)):
#    print(times[cont])
# for pos, time in enumerate(times):
#    print(f'{time} ficou na posição {pos}.')
print('-=-' * 20)
print(f'Lista de times: {times}')
print('-=-' * 20)
print(f'Os primeiros 5 colocados são: {times[0:5]}')
print('-=-' * 20)
print(f'Os ultimos 4 colocados são: {times[-4:]}')
print('-=-' * 20)
print(f'A lista dos times em ordem alfabética é: {sorted(times)}')
print('-=-' * 20)
print(f'A Chapecoense se encontra na {times.index("Chapecoense")+1} posição')














