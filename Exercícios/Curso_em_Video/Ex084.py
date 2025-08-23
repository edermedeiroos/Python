# Faça um programa que leia o nome e peso de várias pessoa guardando tudo isso em uma lista. No final mostre:
# Quantas pessoas foram cadastradas | Uma listagem com as pessoas mais pesadas | Uma listagem com as pessoas mais leves
print('ANALISE DE PESOS COM VARIAS LISTAS')
print()
print('*'*50)
print()
cont = 0
cadastro = []
tempo = []
maior = menor = 0
while True:
    cont += 1
    tempo.append(str(input(f'Nome da pessoa {cont}: ')))
    tempo.append(float(input(f'Peso da pessoa {cont}: ')))
    if len(cadastro) == 0:
        maior = menor = tempo[1]
    else:
        if tempo[1] > maior:
            maior = tempo[1]
        if tempo[1] < menor:
            menor = tempo[1]
    cadastro.append(tempo[:])
    tempo.clear()
    continuar = input('Quer continuar? [S/N]: ').strip().upper()
    if continuar in 'NAO':
        break
print()
print(f'Você cadastrou {len(cadastro)} pesssoas')
print(f'A pessoa mais pesada tem {maior} - ', end='')
for p in cadastro:
    if p[1] == maior:
        print(f'{p[0]}', end=' | ')
print()
print(f'A pessoa mais leve tem {menor} - ', end='')
for p in cadastro:
    if p[1] == menor:
        print(f'{p[0]}', end=' | ')

