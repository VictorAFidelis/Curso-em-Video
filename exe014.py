# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input('Informe a temperatura em C: '))
fah = ((9 * celsius) / 5) + 32
print('A temperatura em C é {} e em Fahrenheit é {}'.format(celsius, fah))