# DICIONÁRIOS
# SEMELHTANTES A TUPLAS E LISTAS, PORÉM PODEMOS COLOCAR OS ÍNDICES COMO PALAVRAS

pessoas = {
    'Nome': 'Eder',
    'Sexo': 'Masculino',
    'Idade': 15
    }
print(pessoas)
print(pessoas['Nome'])
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos')
print(pessoas.keys())  # Mostra os indíces de determinado dicionário
print(pessoas.values())  # Mostra os items dentro dos indíces
print(pessoas.items())  # Mostra tanto indíces como items
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()
del pessoas['Sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()
pessoas['Peso'] = 60
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Estado: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())  # Utilizamos o .copy() como o [:] de dicionários
print(brasil)
print()
from operator import itemgetter
numeros = {'um': 1, 'dois': 2, 'tres': 3, 'quatro': 4, 'cinco': 5}
ordenado = sorted(numeros.items(), key=itemgetter(1))  # Utilizamos o modulo uperator para ordenar dicionarios
print(ordenado)

# DICIONÁRIOS COMPOSTOS
# Podemos adicionar listas dentro de listas

pessoa = {
    'Nome': 'Eder',
    'Hobbys': {
        'Segunda': 'Jogos',
        'Terça': 'Futebol',
        'Quarta': 'Volei'
    },
    'Cozinhar': 'Arroz'
}
print(pessoa['Hobbys']['Quarta'])
for coisa, oque in pessoa.items():
    print(coisa, oque)
for coisa, oque in pessoa['Hobbys'].items():
    print(coisa, oque)

# MÉTODOS ÚTEIS

import copy

len(pessoa) # len - Contagem do número de chaves
pessoa.keys() # keys - iterável com as chaves
pessoa.values() # values - iterável com os valores das chaves
pessoa.items() # items - iterável com chaves e valores
pessoa.setdefault('Idade', 'Não existia') # setdefault - adiciona valor se a chave não existe
pessoa.copy() # copy - retorna uma cópia rasa (shallow copy)
copy.deepcopy(pessoa) # atravéz do módulo copy podemos fazer uma cópia profunda (deep copy)
pessoa.get('Nome', 'Não existe') # get - obtém uma chave | Caso não exista retorna segundo parâmetro [None]
pessoa.pop('Nome') # pop - Apaga um item com a chave especificada (del)
pessoa.popitem() # popitem - Apaga o último item adicionado
pessoa.update({
    'Nome': 'Giovana',
    'Profissão': 'Dev'
}) # update - Atualiza ou cria itens em um dicionário 

# DICTIONARY COMPREHENSION
# Criação de dicionários a partir de iteráveis

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

dc = {
    chave: valor.upper() # Valor da chave será maiúsculo caso:
    if isinstance(valor, str) else valor # isntancia do valor seja uma string
    for chave, valor # Para cada chave e valor em produto.items() caso:
    in produto.items()
    if chave != 'categoria' # a chave não seja 'categoria'
}