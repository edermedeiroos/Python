# Crie um algoritimo que leia um número e mostre o seu dobro,
# triplo, e raiz quadrada
n = int(input('digite um número '))
dn = n*2
tn = n*3
rn = n**(1/2)
print('analizando o número {} \nSeu dobro será {} '.format(n, dn), end='')
print('\nSeu triplo será {} \nE sua raíz quadrada será {}'.format(tn, rn))