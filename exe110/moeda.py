def dobro(p=0, formato=False):
    '''
    :param p: Valor adicionado
    :param formato: Se será utilizado a formatação padrão
    :return: False - sem formatação / True - formatado
    '''
    resp = p * 2
    return resp if formato is False else moeda(resp)


def metade(p=0, formato=False):
    resp = p / 2
    return resp if formato is False else moeda(resp)


def aumentar(p=0, t=0, formato=False):
    resp = p + (p * t / 100)
    return resp if formato is False else moeda(resp)


def diminuir(p=0, t=0, formato=False):
    resp = p - (p * t / 100)
    return resp if formato is False else moeda(resp)


def moeda(p = 0, moeda = 'R$ '):
    '''
    -> Função para padronizar os valores e moedas nas mensagens.
    :param preço: valor do produto
    :param moeda: qual moeda será usada. Padrão colocamos real R$
    :return: moeda e o valor(R$100,00)
    '''
    return f'{moeda}{p:>.2f}'.replace('.', ',')

def resumo(p, a, r,):
    '''
    -> Função para mostrar valor adicionado, metade do valor, dobro do valor,
     aumento e redução definidos pelo usuário.
    :param p: Valor ou preço do produto
    :param a: Porcentagem a ser aumentada
    :param r: Porcentagem a ser reduzida
    :return: Retona os valores das operações alinhadas.
    '''
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Dobro do Preço: \t{dobro(p, True)}')
    print(f'Metade do Preço: \t{metade(p, True)}')
    print(f'{a}% de Aumento: \t{aumentar(p, a, True)}')
    print(f'{r}% de Redução: \t{diminuir(p, r, True)}')
