# Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta neessária
# para pintá-la sabendo que a cadas litro de tinta, pinta uma área de 2m2
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
tinta = área / 2
print(f'A sua parede tem a dimensão de {largura}x{altura} e sua área é de {area}m2.')
print(f'Para pintar a sua parede irá precisar de {tinta} litros de tinta')
