# Crie um programa que cria uma matriz 3x3 e preencha com valores lidos pelo teclado
# No final mostre a matriz na tela com a formatação correta
print('MATRIZ')
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
