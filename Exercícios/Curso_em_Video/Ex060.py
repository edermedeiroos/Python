# Faça um programa que leia um número qualquer, e mostre seu fatorial
# tente fazer com while e for
print('FATORIAL')
print()
print('*'*50)
print()
n = int(input('Digíte um valor: '))
c = n
f = 1
print('CALCULANDO {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))