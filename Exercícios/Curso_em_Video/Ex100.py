# Faça um programa que tenha uma lista chamada números e dua funções chamadas sorteia() e somapar().
# A primeira função vai sortear 5 números e vai coloca-los dentro da lista
# A segunda função vai mostrar a soma de todos os valores pares sorteados pela função anterior
from random import randint


def sorteia():
    for c in range(0, 5):
        n = randint(0, 10)
        nums.append(n)


def somapar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Os valores aleatorizados foram {lista}\n')
    print(f'    • A soma dos valores aleatórios pares é: {soma}')


print('SOMA PAR ALEATÓRIA | FUNÇÃO')
print()
print('-'*50)
print()
nums = list()
sorteia()
somapar(nums)
