# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Por quantos dias o carro foi alugado: '))
km = float(input('Quantos km foram percorridos com esse carro: '))
diaria = dias * 60
kms = km * 0.15
total = diaria + kms
print('Seus custos são: \nAluguel: R${} \nKilometragem: R${:.2f} \nTotal: {:.2f}'.format(diaria, kms, total))




