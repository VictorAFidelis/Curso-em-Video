# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

valores = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0: # inserindo o primeiro valor
        valores.append(n)
        print('Adicionado ao final da lista...')
    elif n > valores[-1]: # para o maior número ele vai entrar no final
        valores.append(n)
        print('Adicionado ao final da lista...')
# para simplificar posso usar if c == 0 or n > lista[-1]:
    else:
        pos = 0
        while pos < len(valores): # lendo da posição 0 até a ultima posição
            if n <= valores[pos]: # número que eu quero inserir é menor ou igual aos da lista
                valores.insert(pos, n) # insere na posição os números
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print(f'Os números digitados em ordem foram {valores}')

