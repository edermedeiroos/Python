# Faça um programa que leia o peso de 5 pessoas, e no final mostre qual foi o maior e o menor peso lido
print('PESOS')
print()
print('*'*50)
print()
pesos = [float(input('Peso da {}º pessoa: '.format(a))) for a in range(1, 6)]
print('O maior peso foi de {}Kg!\n'
      'O menor foi de {}Kg!'.format(max(pesos), min(pesos)))
