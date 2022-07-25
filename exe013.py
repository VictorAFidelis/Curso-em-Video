# Faça um algoritmo que leia um salário de um funcionario e mostre seu novo salário com 15% de aumento
salario = float(input('Qual o seu salario atual: R$ '))
novo = salario + (salario * 15 /100)
print(f' O seu salario atual é R${salario:.2f} e com o novo aumento será de R${novo:.2f}')


