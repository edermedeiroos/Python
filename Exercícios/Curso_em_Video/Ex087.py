# Aprimore o desafio anterior, mostrando no final:
# A soma de todos os valores pares | A soma dos valores da terceira colunas | O maior valor da segunda linha
print('MATRIZ | DADOS ADICIONAIS')
print()
print('*'*50)
print()
lista = [[], [], []]
for b in range(0, 3):
    for c in range(0, 3):
        lista[b].append(int(input(f'Digíte um valor para [{b}, {c}]: ')))
print('-='*25)
for a in range(0, 3):
    for d in range(0, 3):
        print(f'[{lista[a][d]:^5}]', end='')
    print()
print('-='*25)
somapar = 0
for e in range(0, 3):
    for f in lista[e]:
        if f % 2 == 0:
            somapar += f
print(f'A soma de todos os valores pares é {somapar}')
soma3coluna = 0
for g in range(0, 3):
    for h, i in enumerate(lista[g]):
        if h == 2:
            soma3coluna += i
print(f"A soma dos valores da 3' coluna é {soma3coluna}")
print(f"O maior valor da 2' linha é {max(lista[1])}")