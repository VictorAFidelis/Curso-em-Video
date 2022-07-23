# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota '))
média = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, Sua média final foi {:.1f}'. format(n1, n2, média))
if média < 5:
    print('Você foi REPROVADO!')
elif 7 > média >= 5:
    print('Você está em RECUPERAÇÃO!')
elif média >= 7:
    print('PARABÉNS, você foi APROVADO!!!')
