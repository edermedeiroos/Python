# Crie um programa que leia um número inteiro qualque e mostre se ele é par ou ímpar
num = int(input('Digíte um número: '))
if num/2 == int(num/2):
    print('O número {} é par'.format(num))
else:
    print('O número {} é ímpar'.format(num))