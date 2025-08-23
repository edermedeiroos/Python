# Faça um programa que leia um número inteiro, e diga se ele é ou não um número primo
print('NÚMEROS PRIMOS')
print()
print('*'*50)
print()
n = int(input('Digíte um número inteiro qualquer: '))
tot = 0
print()
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[1;032m', end='')
        tot += 1
    else:
        print('\033[1;031m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(n, tot))
if tot == 2:
    print('Portanto é PRIMO')
else:
    print('Portanto NÃO é PRIMO')
