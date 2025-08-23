# Crie um programa que leia vários valores e coloque-os numa lista, depois disso
# Crie duas listas extras,  um com valores pares, e outra com valores impares. No final mostre as 3
print('LISTAS MULTIPLAS')
print()
print('*'*50)
print()
lista = []
listapar = []
listaimpar = []
while True:
    n = (int(input('Digite um valor: ')))
    lista.append(n)
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
    continuar = input('Quer continuar ? [S/N] ').strip().upper()
    if continuar in 'NAO':
        break
print()
print(f'Lista com todos os valores: {lista}')
print(f'Lista com valores pares: {listapar}')
print(f'Lista com valores impares: {listaimpar}')

# Poderiamos varrer a lista também da forma: for i, v in enumerate(lista):
#                                                if v % 2 == 0:
#                                                    listapar.append(v)
#                                                elif v % 2 == 1:
#                                                    listaimpar.append(v)
