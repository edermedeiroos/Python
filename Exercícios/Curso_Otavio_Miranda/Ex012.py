lista = ['Eder', 'Giovana', 'Dara', 'Marilda', 'Marcelino', 'Tica']
for i, nome in enumerate(lista):
    print(f'No índice {i} temos o valor {nome}')

for nome in lista:
    print(f'No índice {lista.index(nome)} temos o valor {nome}')