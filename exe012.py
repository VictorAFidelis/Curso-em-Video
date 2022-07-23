# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com desconto de 5%..

prod = float(input('Qual o preço do produto: R$ '))
des = prod - (prod * 5 / 100)

print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}.'. format(prod, des))


