# Faça um programa que leia 5 valores numéricos e guarde numa lista
# No final mostre qual foi o maior e menor valor digitado, e mostre suas respectivas posições na lista
print('MAIOR E MENOR | LISTA')
print()
print('*'*50)
print()
lista = list()
maior = 0
menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para posição {c + 1}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print()
print(f'O maior valor digitado foi {max(lista)} na posição: ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i + 1}...', end='')
print()
print(f'E o menor valor digitado foi {min(lista)} na posição: ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i + 1}...', end='')
print()
print('-------------------------------- PROGRAMA ENCERRADO -------------------------------')
