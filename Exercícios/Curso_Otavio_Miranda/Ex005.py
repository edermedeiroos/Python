# Faça um programa que peça ao usuário para digitar um número inteiro,
# informe se este número é par ou ímpar. Caso o usuário não digite um número
# inteiro, informe que não é um número inteiro.

try:
    n = int(input('Digíte um número inteiro: '))
except ValueError:
    print(' • \033[031mERRO\033[m - Isto não é um número inteiro!')
else:
    if n % 2 == 0:
        print(f'O número {n} é par!')
    else:
        print(f'O número {n} é ímpar!')