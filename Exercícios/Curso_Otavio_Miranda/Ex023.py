lista_a = [10, 24, 64, 5.7, 23, 1, 0]
lista_b = [231, 65, 73, 1, 4, 5, 6.23, 9.5]

def lista_soma(lista1, lista2):
    soma = [
        sum(*[indice]) for indice in zip(lista1, lista2)
    ]
    return soma

print(lista_soma(lista_a, lista_b))

from itertools import zip_longest

print([sum(*[indice]) for indice in zip_longest(lista_a, lista_b, fillvalue=0)])