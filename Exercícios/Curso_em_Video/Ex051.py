# Desenvolva um programa que leia o primeiro termo e a razão de uma P.A
# No final, mostre os 10 primeiro termos dessa progressão aritimética
print('PROGRESÃO ARITIMÉTICA')
print()
print('*'*50)
print()
n = int(input('Primeiro termo da P.A: '))
r = int(input('Razão da P.A: '))
print()
print('os 10 primeiros termos da progressão aritimética do número {} com razão {} são:'.format(n, r))
print('-'*50)
for pa in range(n, n + r * 10, r):
    print('{} | '.format(pa), end='')
print()
print('-'*50)
