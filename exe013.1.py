# Um produto de tem um valor para venda. Se o pagamento for a vista recebe 5% de deconto. A prazo terá 8% de acréscimo.

prod = float(input('Qual o valor do produto: R$ '))
vista = prod - (prod * 5 / 100)
prazo = prod + (prod * 8 / 100)
print('As formas de pagamento para esse produto são:\nA vista {:.2f} \nPrazo {:.2f}'.format(vista, prazo))