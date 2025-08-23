# Faça um programa que leia uma frase e mostre:
# 1 - Quantas vezes aparece a letra "a"
# 2 - Em que posição ela aparece na primeira vez
# 3 - Em que posição ela aparece a ultima vez
f = str(input('Digíte uma frase: ')).strip()
frase = f.upper()
frase2 = ''.join(frase.split())
print('A frase "{}" contém {} letras "a"'.format(f, frase.count('A')))
print('A letra "a" aparece pela primeira vez na posição {}'.format(int(frase2.find('A')+1)))
print('A letra "a" aparece pela ultima vez na posição {}'.format(int(frase2.rfind('A')+1)))
