# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um
# módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de
# funcionar como a função imputa(), mas com uma validação de dados para aceitar
# apenas valores que seja monetários.
from exe112.UtilidadesCeV import moeda
from exe112.UtilidadesCeV import dados
p = dados.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(p, 30, 20)
