# GENERATOR
# Funções que sabem pausar o iterador sem carrega-lo inteiro na memória (yield)
# É possível apenas a iteráveis imutaveís (ex: tupla)
# Não possui índices, valores, tamanho, etc. Apenas o próximo valor (next())

import sys

lista = [n for n in range(1000000)] # Carrega todos os valores presentes no range
generator = (n for n in range(1000000)) # Carrega apenas o primeiro valor do range 

print(sys.getsizeof(lista)) # Bytes da lista carregada por completo
print(sys.getsizeof(generator)) # Bytes do generator 

print(generator) # Mostra o objeto localizado na memória
print(next(generator)) # Mostra o proximo valor do iterador
print(next(generator))

def generator():
    for n in range(10):
        yield n # Faz a pausa em cada valor no range(10)

def generator2():
    yield from generator() # Recebe as pausas do outro generator()
    for n in range(10, 20):
        yield n # Faz a pausa em cada valor no range(10, 20)

gen = generator2() # Generator2() Fica com as pausas no range(20)

for rep in range(20):
    print(next(gen))