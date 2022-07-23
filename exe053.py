#Crie um programa que leia uma
# frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

f = str(input('Digite uma frase: ')).strip().upper()
p = f.split()
junto = ''.join(p)
'''inverso = '' '''
inverso = junto [:: -1]
'''for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada não é um Palídromo!')

