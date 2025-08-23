# Escreva um programa que leia um número inteiro qualquer e peça para o usúario
# escolher qual será a base de conversão: 1 = binário | 2 = octal | 3 = hexadecimal
print('CONVERSÃO NUMÉRICA')
print()
print('*'*50)
print()
print('Bases de conversão disponíveis: 1 para binários | 2 para octal | 3 para hexadecimal')
print()
n = int(input('Digíte um número inteiro qualquer: '))
bc = int(input('Base de conversão escolhida: '))
print()
print('\033[1;34mCONVERTENDO...\033[m')
print()
if bc == 1:
    print('O número {} em binário é {}.'.format(n, bin(n)[2:]))
elif bc == 2:
    print('O número {} em octal é {}.'.format(n, oct(n)[2:]))
elif bc == 3:
    print('O número {} em octal é {}.'.format(n, hex(n)[2:]))
else:
    print('Opção inválida, tente novamente')
