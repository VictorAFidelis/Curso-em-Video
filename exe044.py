#Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
print('============= LOJÃO DO FIDELIS ==========')
c = int(input('Preco das Compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista no cartão
[ 3 ] 2x no cartão sem juros
[ 4 ] até 10 no cartão com juros''')
o = int(input('Qual a sua opção? '))
if o == 1:
    total = c - (c * 10 / 100)
elif o == 2:
    total = c
elif o == 3:
    total = c
    parcela = c / 2
    print(f'Sua compra será parcelada em 2 vezes de R$ {parcela:.2f}')
elif o == 4:
    total = c + (c * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc} vezes de R$ {parcela:.2f}')
    print(f'Sua compra de R$ {c:.2f} vai custar R$ {total:.2f} no final.')
else:
    o = 0
    print('OPÇÃO INVALIDA de pagamento, tente novamente!')



















