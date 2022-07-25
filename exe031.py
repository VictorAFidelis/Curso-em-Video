# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
v = float(input('Qual a distancia da sua viagem? '))
if v <= 200:
    passagem_curta = v * 0.50
    print(f'O valor da passagem será de R$ {passagem_curta:.2f}')
else:
    passagem_longa = v * 0.45
    print(f'O valor da passagem será R$ {passagem_longa:.2f}')





