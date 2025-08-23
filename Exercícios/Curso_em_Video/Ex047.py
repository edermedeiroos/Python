# Crie um programa que mostre todos os números pares num intervalo de 1 à 50
print('NÚMEROS PARES')
print()
print('*'*50)
print()
print('Números pares de 1 á 50:')
for num in range(0, 51, 2):
    print('{} |'.format(num), end=' ')
print('Acabou.')
