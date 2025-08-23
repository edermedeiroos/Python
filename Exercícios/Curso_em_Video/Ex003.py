# Crie um programa que some dois números
n1 = int(input('Digite número: '))
n2 = int(input('Digite outro número: '))
s = n1+n2
print('A soma de {}{}{} mais {}{}{} é igual a {}{}{}'.format('\033[1;32m', n1, '\033[m', '\033[1;33m',  n2, '\033[m', '\033[1;34m', s, '\033[m'))
