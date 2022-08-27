#Crie um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe
# esse módulo e use algumas dessas funções.

import moeda
p = float(input('Digite um valor: R$ '))
print(f'O dobro do valor R$ {p} é  {moeda.dobro(p)}')
print(f'A metade do valor R$ {p} é {moeda.metade(p)}')
print(f'Aumentando 10%, o valor de {p}, ficará {moeda.aumentar(p, 10)}')
print(f'Diminuindo em 13%, o valor de {p} será {moeda.diminuir(p, 13)}')
