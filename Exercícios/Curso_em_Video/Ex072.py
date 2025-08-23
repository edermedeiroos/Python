# Crie um programa que tenha uma tupla totalmente preenchida de 0-20
# Seu programa deverá ler um número de 0-20, e dize-lo por extenso
print('LEITOR POR EXTENSO')
print()
print('*'*50)
print()
n = int(input('Digíte um número de 0-20: '))
while n > 20 or n < 0:
    n = int(input('Digíte um número de 0-20: '))
nextenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
            'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
            'doze', 'treze', 'quartorze', 'quinze', 'dezesseis',
            'dezessete', 'dezoito', 'dezenove', 'vinte')
print()
print(f'O número {n}, escrito em estenso é {nextenso[n]}.')
print()
print('-------------------------------- PROGRAMA ENCERRADO --------------------------------')
