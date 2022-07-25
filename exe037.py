# Escreva um programa em Python que leia um número inteiro qualquer e
# peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digite um número inteiro: '))
print('''Escolha a sua base para conversão
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converte para HEXADECIMAL''')
opçao = int(input('Sua opção: '))
if opçao == 1:
    print(f'{num} convertido para BINARIO é igual {bin(num)}')
elif opçao == 2:
    print(f'{num} convertido em OCTAL é igual a {oct(num)}')
elif opçao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual {hex(num)}')
else:
    print('Opção inválida, tente novamente.')



