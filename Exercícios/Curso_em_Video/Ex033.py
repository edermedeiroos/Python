# Faça um programa que leia 3 números, e mostre qual deles é o maior, e qual é o menor
n1 = int(input('Digíte um número: '))
n2 = int(input('Digíte um segundo número: '))
n3 = int(input('Digíte um terceiro número: '))
if n1 > n2 > n3:
    print('O maior número é {}, e o menor {}.'.format(n1, n3))
if n1 > n3 > n2:
    print('O maior número é {}, e o menor {}.'.format(n1, n2))
if n2 > n1 > n3:
    print('O maior número é {}, e o menor {}.'.format(n2, n3))
if n2 > n3 > n1:
    print('O maior número é {}, e o menor {}.'.format(n2, n1))
if n3 > n1 > n2:
    print('O maior número é {}, e o menor {}.'.format(n3, n2))
if n3 > n2 > n1:
    print('O maior número é {}, e o menor {}.'.format(n3, n1))
