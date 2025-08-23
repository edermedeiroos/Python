# Crie um programa que simulo o funcionamento de um caixa eletrônico
# No início, pergunte ao usúario qual o valor a ser sacado
# e o programa deverá informar quantas cédulas de cada valor serão entregues
# Cédulas: R$50 | R$20 | R$10 | R$1
print('BANCO')
print()
print('*'*50)
print()
print('--- CÉDULAS DISPONÍVEIS [50, 20, 10, 1]')
valor = int(input('Valor a ser sacado: R$'))
n50 = (valor // 50)
n20 = ((valor - n50 * 50) // 20)
n10 = ((valor - n50 * 50 - n20 * 20) // 10)
n1 = ((valor - n50 * 50 - n20 * 20 - n10 * 10) // 1)
print()
print('-'*50)
print('| {} cédulas de 50 |\n| {} cédulas de 20 |\n| {} cédulas de 10 |\n| {} cédulas de 1 |'.format(n50, n20, n10, n1))
print('-'*50)
print()
print('------------------------- TENHA UM BOM DIA! -------------------------')
print()