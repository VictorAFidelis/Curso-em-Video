def dobro(p):
    resp = p * 2
    return resp


def metade(p):
    resp = p / 2
    return resp


def aumentar(p, t):
    resp = p + (p * 10 / 100)
    return resp


def diminuir(p, t):
    resp = p - (p * 13 / 100)
    return resp

def moeda(preço = 0, moeda = 'R$ '):
    '''
    -> Função para padronizar os valores e moedas nas mensagens.
    :param preço: valor do produto
    :param moeda: qual moeda será usada. Padrão colocamos real R$
    :return: moeda e o valor(R$100,00)
    '''
    return f'{moeda}{preço:>.2f}'.replace('.', ',')

