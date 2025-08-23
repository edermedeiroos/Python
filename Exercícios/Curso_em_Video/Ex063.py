# Escreva um programa que leia um n inteiro, e mostre na tela os n primeiros termos
# da sequência de Fibonacci
print('SEQUÊNCIA DE FIBONACCI')
print()
print('*'*50)
print()
n = int(input('Digíte o número de termos a ser mostrado: '))
print()
termo1 = 0
termo2 = 1
termo3 = 1
cont = 3
print(termo1, end=' | ')
if n == 2 or n > 2:
    print(termo2, end=' | ')
while n >= cont:
    cont += 1
    print(termo1 + termo2, end=' | ')
    termo1 = termo2
    termo2 = termo3
    termo3 = termo1 + termo2
print()
print()
print('------------------------ PROGRAMA ENCERRADO ------------------------')
