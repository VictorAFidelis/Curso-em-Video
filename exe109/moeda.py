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
    resp = p + (p * 10 / 100)
    return resp if formato is False else moeda(resp)


def diminuir(p=0, t=0, formato=False):
    resp = p - (p * 13 / 100)
    return resp if formato is False else moeda(resp)


def moeda(p = 0, moeda = 'R$ '):
    '''
    -> Função para padronizar os valores e moedas nas mensagens.
    :param preço: valor do produto
    :param moeda: qual moeda será usada. Padrão colocamos real R$
    :return: moeda e o valor(R$100,00)
    '''
    return f'{moeda}{p:>.2f}'.replace('.', ',')
