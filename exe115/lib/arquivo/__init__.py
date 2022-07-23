from exe115.lib.interface import *
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') # rt significa read text.
        a.close()
    except FileNotFoundError: # arquivo não encontrado
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') # wt+ signfica escrever um arquivo de texto. Sinal de +,
        # signifca se o arquivo não existe ele é criado
        a.close()
    except:
        print('Houve um erro na criação do arquivo!.')
    else:
        print(f'Arquivo {nome} criado com sucesso!.')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao abrir o arquivo!.')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='<desconhecido>', idade=0):
    try:
        a = open(arq, 'at') # at, a significa append de adicionar
    except:
        print('Houve um Erro na abertura do arquivo!.')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print('Houve um Erro na hora de escrever os dados!.')
        else:
            print(f'Novo cadastro de {nome} adicionado com sucesso!.')
            a.close()






