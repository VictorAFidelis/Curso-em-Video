# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

v = float(input('Qual a distancia da sua viagem? '))
if v <= 200:
    pas = v * 0.50
    print('O valor da passagem será de R$ {:.2f}'.format(pas))
else:
    pa = v * 0.45
    print('O valor da passagem será R$ {:.2f}'.format(pa))




