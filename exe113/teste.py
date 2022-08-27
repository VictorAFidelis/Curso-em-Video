# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um
# módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de
# funcionar como a função imputa(), mas com uma validação de dados para aceitar
# apenas valores que seja monetários.
from exe113.UtilidadesCeV import dados
n = dados.leiaInt('Digite um número inteiro: ')
print(f'O número que você digitou foi {n}')
f = dados.leiaFloat('Digite um número real ')
print(f'O número real que você digitou foi {f}')
