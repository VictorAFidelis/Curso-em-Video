# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
t = int(input('Digite um número para ver sua tabuada: '))
print('-=-' * 12)
for c in range(0, 11):
    print('{} x {} = {}'.format(c, t, (c * t)))
print('-=-' * 12)






