# Crie um programa que leia vários números inteiros. No final mostre a média entre todos os valores
# e qual foi o maior e menor valor lido. O programa deverá perguntar ao usúario se ele quer ou
# não continuar a digitar valores.
print('NÚMERAL MAIOR E MÉDIA')
print()
print('*'*50)
print()
n1 = int(input('Digíte um valor: '))
n2 = int(input('Digíte um valor: '))
n3 = 0
n4 = 0
media = (n1+n2)/2
media2 = n1 + n2
media3 = 0
maior1 = max(n1, n2)
menor1 = min(n1, n2)
cont = 2
continuar = input('Quer continuar a digitar valores? ').strip().upper().replace('Ã', 'A')
while continuar not in 'NAO':
    n3 = int(input('Digíte um valor: '))
    continuar = input('Quer continuar a digitar valores? ').strip().upper().replace('Ã', 'A')
    cont += 1
    media3 = (media2 + n3)/cont
    media2 = media2 + n3
    maior2 = max(n1, n2, n3)
    menor2 = min(n1, n2, n3)
    if maior2 > maior1:
        maior1 = maior2
    elif maior2 < maior1:
        maior1 = maior1
    else:
        maior1 = maior2
    if menor2 < menor1:
        menor1 = menor2
    elif menor2 > menor1:
        menor1 = menor1
    else:
        menor1 = menor2
if cont == 2:
    print()
    print('A média dos {} valores digitados é: {} | O maior valor digitado foi {} e o menor {}.'.format(cont, media, maior1, menor1))
    print()
    print('---------------------------------- PROGRAMA ENCERRADO ----------------------------------')
else:
    print()
    print('A média dos {} valores digitados é: {} | O maior valor digitado foi {} e o menor {}'.format(cont, media3, maior1, menor1))
    print()
    print('---------------------------------- PROGRAMA ENCERRADO ----------------------------------')
