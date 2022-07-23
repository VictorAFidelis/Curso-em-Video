# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo
# agora a possibilidade da digitação de um número de tipo inválido. Aproveite e
# crie também uma função leiaFloat() com a mesma funcionalidade.
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;031m ERRO! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;031mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            f = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;031mERRO! Digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return f


#programa principal
n = leiaInt('Digite um número inteiro: ')
print(f'O número que você digitou foi {n}')
f = leiaFloat('Digite um número real ')
print(f'O número real que você digitou foi {f}')

