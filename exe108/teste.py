# Adapte o código do desafio #107, criando uma função adicional chamada
# moeda() que consiga mostrar os números como um valor monetário formatado
from exe108 import moeda
p = float(input('Digite um valor: R$ '))
print(f'O dobro do valor R$ {moeda.moeda(p)} é  {moeda.moeda(moeda.dobro(p))}')
print(f'A metade do valor R$ {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'Aumentando 10%, o valor de {moeda.moeda(p)}, ficará {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuindo em 13%, o valor de {moeda.moeda(p)} será {moeda.moeda(moeda.diminuir(p, 13))}')











