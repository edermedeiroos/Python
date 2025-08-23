# Crie um programa que leia vários números inteiros. O programa só para quando digitado o valor 999
# No final mostre quantos números foram digitados e qual foi a soma entre eles
# desconsiderando o flag (999)
print('LEITOR NÚMERO E SOMATÓRIA')
print()
print('*'*50)
print()
cont = 0
nPrimeiro = int(input('Digíte um valor | [999] para sair: '))
nDiverso = 0
soma = nPrimeiro
if nPrimeiro != 999:
    while nDiverso != 999:
        cont += 1
        nDiverso = int(input('Digíte um valor | [999] para sair: '))
        soma += nDiverso
    print()
    print('A soma dos {} valores digitados foi: {}'.format(cont, soma - 999))
    print()
    print('----------------------- PROGRAMA ENCERRADO -----------------------')
else:
    print()
    print('----------------------- PROGRAMA ENCERRADO -----------------------')
