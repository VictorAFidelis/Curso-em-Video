# Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta neessária
# para pintá-la sabendo que a cadas litro de tinta, pinta uma área de 2m2

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
área = largura * altura
tinta = área / 2
print('A sua parede tem a dimensão de {}x{} e sua área é de {}m2.'.format(largura, altura, área))
print('Para pintar a sua parede irá precisar de {} litros de tinta'.format(tinta))
