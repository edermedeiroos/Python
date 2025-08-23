# Crie um programa que leia um número Real qualquer e mostre sua porção inteira
import math
n = float(input('Digite um número real qualquer: '))
print ('o valor digitado foi {}, e sua porção inteira é: {}'.format(n, math.floor(n)))