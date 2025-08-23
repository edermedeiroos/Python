# Crie um programa em uma tupla única, que guarde nomes de produtos e seus respectivos preços
# No final, mostre uma listagem de preços, organizando os dados de forma tabular
print()
lista = ('Arroz', 15.00, 'Feijão', 10.00, 'Banana', 5.50, 'Energético', 8.49, 'Picanha', 100.00, 'Balas', 0.35,
         'Chiclete', 2.89, 'Processador', 1253.45)
print('-'*55)
print(f'{"LISTAGEM DE PREÇOS":^55}')
print('-'*55)
for c in range(0, len(lista), 2):
    print(lista[c], '.' * (40 - len(lista[c])), f'R${lista[c+1]:>7}')
print('-'*55)
