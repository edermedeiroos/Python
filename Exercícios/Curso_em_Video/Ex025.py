# Crie um programa que leia o nome de uma pessoa, e diga se ela tem "Silva" no nome
n = str(input('Digíte seu nome completo: '))
ns = n.upper()
print('Seu nome tem Silva?\n{}'.format('SILVA' in ns))
