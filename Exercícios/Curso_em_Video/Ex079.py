# Crie um programa onde o usúario possa digitar vários valores e os cadastre numa lista
# Caso o número ja exista na lista ele não será adicionado
# No final será exibido todos os valores únicos digitados em ordem crescente
print('CADASTRADOR NUMÉRICO | LISTA')
print()
print('*'*50)
print()
lista = [int(input('Digite um valor: '))]
print('Valor adicionado com sucesso!')
while True:
    continuar = input('Quer continuar? [S/N]').strip().upper()
    if continuar not in 'S':
        break
    lista.append(int(input('Digite um valor: ')))
    if lista[-1] in lista[:-1]:
        lista.pop(-1)
        print('Valor ja adicionado... - RETIRANDO -')
    else:
        print('Valor adicionado com sucesso!')
print(f'Você digitou os valores {lista}')
print(f'Organizados de forma crescente são {sorted(lista)}')
