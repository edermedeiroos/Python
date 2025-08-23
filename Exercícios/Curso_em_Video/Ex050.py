# Desenvolva um programa que leia 6 números inteiros, e mostre a soma apenas dos números pares
print('SOMA DE NÚMEROS PARES PELO USÚARIO')
print()
print('*'*50)
print()
soma = 0
cont = 0
for n in range(1, 7):
    num = int(input('Digíte o valor {}: '.format(n)))
    if num % 2 == 0:
        soma += num
        cont += 1
print()
print('A soma dos {} valores pares digitados é: {}'.format(cont, soma))
