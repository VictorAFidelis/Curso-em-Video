# Um produto de tem um valor para venda. Se o pagamento for a vista recebe 5% de deconto. A prazo terá 8% de acréscimo.
produto = float(input('Qual o valor do produto: R$ '))
vista = produto - (produto * 5 / 100)
prazo = produto + (produto * 8 / 100)
print(f'As formas de pagamento para esse produto são:\nA vista {vista:.2f} \nPrazo {prazo:.2f}')
