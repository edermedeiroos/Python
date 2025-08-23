# IterTools | Módulo python com funções adicionais de iterações

import itertools

# COUNT()
# Contador infinito | Range sem fim
contador = itertools.count()

# COMBINATIONS()
# Combinações possíveis de determinado iteravel com um numero de iterações
pessoas = ['Eder', 'Marilda', 'Dara', 'Marcelino']
combinacao = itertools.combinations(pessoas, 2)

# PERMUTATIONS
# Combinações possíveis de determinado iteravel com um numero de iterações com o fator ordem importando
permutacao = itertools.permutations(pessoas, 2)

# PRODUCT
# Produtos possíveis de combinações dentro dos iteráveis
loja = [
    ['Preta', 'Branca'],
    ['Masculino', 'Feminino', 'Unissex'],
    ['Algodão', 'Poliéste']
]
produto = itertools.product(*loja)

# GROUPBY
# Agrupa os valores de um iteravel de acordo com determinada condição
alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

def ordena(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key=ordena)
grupos = itertools.groupby(alunos_agrupados, key=ordena)

for nota, grupo in grupos:
    print(nota, *grupo)
