# Crie um programa que leia quanto dinheiro uma pessoa tenha na carteira e mostre quantos Dólares ela pode comprar.
# Considera U$$ 1,00 = R$ 3,27
real = float(input('Qual valor você tem na carteira: R$ '))
dolar = real / 5.44
euro = real / 6.13
print(f'Com R${real:.2f} você pode comprar \nUS${dolar:.2f} e \nE${euro:.2f}')


