# Crie um programa que leia uma frase qualquer, e diga se ela é um palíndromo, desconsiderando os espaços
print('DETECTOR PALÍNDROMO')
print()
print('*'*50)
print()
f = str(input('Digíte uma frase: ')).strip().upper()
palavras = f.split()
junto = ''.join(palavras)
inverso = junto[::-1]
"""inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]"""
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')
