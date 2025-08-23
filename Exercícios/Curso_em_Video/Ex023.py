# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
num  = int(input('Digíte um número inteiro: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('{} unidade(s)'.format(u))
print('{} dezena(s)'.format(d))
print('{} centena(s)'.format(c))
print('{} unidade(s) milhar '.format(m))
