# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Qual a velocidade do carro? '))
if vel > 80:
    print('Você foi multado! Você excedeu o limite permitido que é de 80km/h')
    multa = (vel-80) *7
    print('O valor da sua multa será R$ {:.2f}'.format(multa))
print('Tenha um Bom dia! Dirija com segurança')



