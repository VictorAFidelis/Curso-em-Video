# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e
# vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
def notas(*n, sit=False):
    '''
    -> Função para calcular notas de alunos.
    :param n: notas adicionadas. Pode ser uma ou mais notas
    :param sit: valor adicional, indicando se deve ou adicional a situação
    :return: dicionario com várias informações sobre a situação da turma
    '''
    r = dict()
    r['Quantidade de Notas'] = len(n)
    r['Maior nota'] = max(n)
    r['Menor nota'] = min(n)
    r['Média'] = sum(n) / len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Média'] >= 5:
            r['Situação'] = 'RAZOAVEL'
        else:
            r['Situação'] = 'RUIML'
        return r


#programa principal
resp = notas(3.5, 4.8, 6.75, sit=True)
print(resp)

