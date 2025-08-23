# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seu
# seno, cosseno e tangente
import math
a = float(input('Valor do ângulo em graus: '))
seno = math.sin(math.radians(a))
cosseno = math.cos(math.radians(a))
tangente = math.tan(math.radians(a))
print('-'*12)
print('Seno({}): {:.2f}\nCosseno({}): {:.2f}\nTangente({}): {:.2f}'.format(a, seno, a, cosseno, a, tangente))
print('-'*12)
