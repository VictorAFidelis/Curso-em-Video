# Crie um programa que tenha uma função fatorial() que receba dois
# parâmetros: o primeiro que indique o número a calcular e outro chamado show,
# que será um valor lógico (opcional) indicando se será mostrado ou não na
# tela o processo de cálculo do fatorial.

def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show == True:
            if c == 1:
                print(c, end='=', flush=True)
            else:
                print(c, end='x', flush=False)
            print(f)


n = int(input('Digite um número: '))
show = str(input('Gostaria de ver o fatorial completo?[S/N] ')).upper().strip()
if show == 'S':
    show=True
elif show == 'N':
    show=False
fatorial(n, show)


