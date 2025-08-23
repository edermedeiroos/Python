# Módulos são recursos adicionais ao python
# Usaremos comando import para importar módulos inteiros
# Usaremos from (nome do módulo) import para importar um item específico
# Usamos as para adicionar um nome ao módulo
# Módulos são singleton - Carregados apenas uma vez
# Todas as importações devem ser relativas e permitidas ao __main__ (arquivo.py atual) 

from sys import path
print(*path,  sep='\n') # Mostra o diretório do módulo atual

import random as aleatorizador
aleatorizador.randint(1, 10)

import math
num = int(input('Digite um número'))
print(math.sqrt(num))

# Um módulo é um conjunto de várias funções
# Podemos criar arquivos .py e utiliza-lo como módulos

import moduloteste
num = int(input('Digíte um número: '))
fat = moduloteste.fatorial(num)
dobro = moduloteste.dobro(num)
triplo = moduloteste.triplo(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {dobro}')
print(f'O tripo de {num} é {triplo}')

# Os pacotes formam uma pasta com vários módulos, separando-os por assunto