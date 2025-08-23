from copy import deepcopy
from Módulos.Dados import produtos


novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.10, 2)} # Substitui a key 'preco' para o preco de cada produto com um aumento de 10%
    for p in deepcopy(produtos) # para cada produto numa cópia profunda de produtos
]

produtos_ordenados_por_nome = sorted(
    deepcopy(produtos),
    key=lambda p: p['nome'], # Ordena pela key do 'nome'
    reverse=True # reverso
)

produtos_ordenados_por_preco = sorted(
    deepcopy(produtos),
    key=lambda p: p['preco'] # Ordena pela key do 'preco'
)

for produto in produtos:
    print(f'• O {produto["nome"]} custa R$ {produto["preco"]}')

print('-'*50)

for produto in novos_produtos:
    print(f'• O {produto["nome"]} com um aumento de 10% custa R$ {produto["preco"]}')

print('-'*50)

print('• Os produtos ordenados por nome são:\n')
for produto in produtos_ordenados_por_nome:
    print(f'• O {produto["nome"]} custa R$ {produto["preco"]}')

print('-'*50)

print('• Os produtos ordenados por preço são:\n')
for produto in produtos_ordenados_por_preco:
    print(f'• O {produto["nome"]} custa R$ {produto["preco"]}')
