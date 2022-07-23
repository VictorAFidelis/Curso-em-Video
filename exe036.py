# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
print('-=-' * 10)
print('\033[7;40mBem vindo a Fidelis Cred\033[m')
print('-=-' * 10)
casa = float(input('Qual o valor da casa que você deseja comprar? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
tempo = float(input('Quantos anos você pretende pagar? '))
parcela = casa / (tempo * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R$ {:.2f} em {:.0f} anos '.format(casa, tempo), end='')
print('a prestação sera de R$ {:.2f}'.format(parcela))
if parcela <= minimo:
    print('Seu empréstimo foi \033[1;34mAPROVADO!')
else:
    print('Seu empréstimo foi \033[1;31mNEGADO!')


