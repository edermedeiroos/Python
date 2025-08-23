# Crie um programa onde o usúario possa digitar 7 valores numéricos e cadastre-os em uma lista única
# que mantenha separado os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente
print('PAR E ÍMPAR | LISTA ÚNICA')
print()
print('*'*50)
print()
lista = []
listapar = []
listaimpar = []
npar = 0
nimpar = 0
for c in range(0, 7):
    lista.append(int(input('Digíte um valor: ')))
lista.sort()
print()
for n in lista:
    if n % 2 == 0:
        listapar.append(n)
        npar += 1
for n in lista:
    if n % 2 == 1:
        listaimpar.append(n)
        nimpar += 1
lista.clear()
lista.append(listaimpar)
lista.append(listapar)
print(f'Os números pares digitados foram: {lista[1]}\nOs números ímpares digitados foram: {lista[0]}')
print('-'*20, ' PROGRAMA ENCERRADO ', '-'*20)