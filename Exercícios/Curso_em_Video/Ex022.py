# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1 - o nome com todas as letras maiúsculas
# 2 - o nome com todas as letras minúsculas
# 3 - quantas letras ao todo, sem considerar espaços
# 4 - quantas letras tem o primeiro nome
nome = (input('Digíte seu nome completo: '))
print()
print('Seu nome em maiúsculo: {}'.format(nome.upper()))
print('Seu nome em minúsculo: {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(''.join(nome.split()))))
print('Seu primeiro nome tem {} letras'.format(len(nome.split()[0])))