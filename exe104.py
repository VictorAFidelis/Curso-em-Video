# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input()
# do Python, só que fazendo a validação para aceitar apenas um valor numérico.
def leiaInt(msg):
    '''
    -> Validando se foi digitado um número inteiro
    :param msg: Deve ser digitado u número inteiro
    :return: Informa o número digitado. Caso tenha digitado incorretamente, retorna uma mensagem com erro.
    '''
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número válido. \033[m')
        if ok:
            break
    return valor


#programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n} .')