# Faça um algoritmo que leia um salário de um funcionario e mostre seu novo salário com 15% de aumento

salario = float(input('Qual o seu salario atual: R$ '))
novo = salario + (salario * 15 /100)
print(' O seu salario atual é R${:.2f} e com o novo aumento será de R${:.2f}'.format(salario, novo))


