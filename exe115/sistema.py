from exe115.lib.interface import *
from exe115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Lista de Pessoas Cadastradas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('\033[0;97mSaindo do sistema... Até logo!\033[m')
        break
    else:
        print('\033[0;031mERRO! Digite uma opção válida!\33[m')
    sleep(2)










