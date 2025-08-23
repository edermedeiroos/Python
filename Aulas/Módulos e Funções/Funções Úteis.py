# ISISTANCE()
# Verifica o tipo de dado de determinado item

lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

for item in lista:
    if isinstance(item, set):
        print('SET')

    elif isinstance(item, str):
        print('STR')

    elif isinstance(item, (int, float)):
        print('NUM')

    else:
        print('OUTRO')
        print(f'O item {item} é {type(item)}')

# DIR()
# Checa os métodos utilizados dentro de determinado valor

nome = 'Eder'
dir(nome)

# HASATTR()
# Checa a existência de um método específico dentro do valor

nome = 'Eder'
hasattr(nome, 'upper')

# GETATTR()
# Executa métodos atravéz de strings

nome = 'Eder'
metodo = 'upper'
getattr(nome, metodo)()

# REDUCE()
# Reduz o iteravel a um valor único
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]

total = reduce(lambda acumulador, prod: acumulador + prod['preco'], produtos, 0) # Acumulador começa em 0 e soma com cada 'preco' de cada produto dentro de produtos