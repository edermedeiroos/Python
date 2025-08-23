# Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento
s = float(input('Salário: R$'))
ns = s + (s/100 * 15)
print('Seu novo salário com 15% de aumenta será equivalente a {} reais'.format(ns))
