# Faça um programa que leia o nome completo de uma pessoa e mostre o primeiro, e o ultimo nome dela
n = str(input('Digíte seu nome completo: ')).strip()
print()
nome = n.split()
print('Seu primeiro nome é: {}'.format(n.split()[0]))
print('Seu ultimo nome é: {}'.format(nome[len(nome)-1]))
