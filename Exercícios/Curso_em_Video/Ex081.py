# Crie um programa que leia vários números e coloque numa lista, depois disso mostre:
# Quantos números foram digitados | A lista de valores de forma decrescente | Se o valor 5 está ou não na lista
print('LISTA NUMÉRICA')
print()
print('*'*50)
print()
cont = 0
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    cont += 1
    continuar = str(input('Quer continuar a digitar valores? [S/N] ')).strip().upper()
    if continuar in 'NAO':
        break
print()
print(f'Você digitou {cont} números.')
print(f'A lista em ordem decrescente é: {sorted(lista, reverse=True)}')
if 5 in lista:
    print(f'O valor 5 aparece na lista primeiramente na posição {lista.index(5) + 1}.')
else:
    print('O valor 5 não aparece na lista.')
