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
    print('Sua compra será parcelada em 2 vezes de R$ {:.2f}'.format(parcela))
elif o == 4:
    total = c + (c * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {} vezes de R${:.2f}'.format(totparc, parcela))
else:
    o = 0
    print('OPÇÃO INVALIDA de pagamento, tente novamente!')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(c, total))

















