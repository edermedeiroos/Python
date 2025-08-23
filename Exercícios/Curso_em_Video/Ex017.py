# Faça um programa que leia o comprimento do cateto oposto, e do cateto adjacente
# de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
import math
co = float(input('Valor do cateto oposto: '))
ca = float(input('Valor do cateto adjacente: '))
print('A hipotenusa relativa ao cateto oposto {}, e o cateto adjacente {}, '.format(co, ca),end='')
print('tera o valor de {}.'.format(math.hypot(co,ca)))