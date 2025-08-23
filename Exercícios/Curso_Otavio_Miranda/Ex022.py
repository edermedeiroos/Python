lista_cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_estados = ['BA', 'SP', 'MG', 'RJ']

def func_zipper(lista1, lista2):    
    return list(zip(lista1, lista2)) # Retorna as listas unidas até que um dos iteradores acabe

print(func_zipper(lista_cidades, lista_estados))

from itertools import zip_longest

print(list(zip_longest(lista_cidades, lista_estados))) # Retorna as listas unidas até que o maior dos iteradores acabe