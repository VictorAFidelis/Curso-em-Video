# Modifique as funções que form criadas no desafio 107 para que elas
# aceitem um parâmetro a mais, informando se o valor retornado por elas vai
# ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
from exe109 import moeda
p = float(input('Digite um valor: R$ '))
print(f'O dobro do valor {moeda.moeda(p)} é  {moeda.dobro(p, True)}')
print(f'A metade do valor {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'Aumentando 10%, o valor de {moeda.moeda(p)}, ficará {moeda.aumentar(p, 100, True)}')
print(f'Diminuindo em 13%, o valor de {moeda.moeda(p)} será {moeda.diminuir(p, 13, True)}')
