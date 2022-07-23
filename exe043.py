# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida
print('-=-' * 10)
print('CALCULO DE IMC')
print('-=-' * 10)
peso = float(input('Qual o seu peso? (KG) | '))
altura = float(input('Qual a sua altura? (MT) | '))
IMC = peso / (altura ** 2)
print('Com o peso {} e altura {}, seu IMC é {:.1f}.'.format(peso, altura, IMC))
if IMC < 18.5:
    print('Você está ABAIXO DO PESO')
elif 18.5 <= IMC < 25:
    print('Você está em seu PESO IDEAL')
elif 25 <= IMC < 30:
    print('Você está em SOBREPESO')
elif 30 <= IMC < 40:
    print('Você está em OBESIDADE')
elif IMC >= 40:
    print('Você está em OBESIDADE MORDIBA')



