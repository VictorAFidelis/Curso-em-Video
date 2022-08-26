# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão
print('=' * 30)
print(' 10 TERMOS DE UMA PA')
print('=' * 30)
pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = pt + (10) * r
for c in range(pt, decimo, r):
    print('{} '.format(c), end= '→ ')
print('ACABOU')



