# Crie um programa que tenha uma tupla com várias palavras (não use acentos)
# Depois disso, você deve mostrar para cada palavra quais são suas vogais
print('VOGAIS | TUPLA')
print()
print('*'*50)
print()
palavra = ('MACACO', 'LAPIS', 'EDER', 'GIOVANA', 'GOSTOSA', 'CASAMENTO', 'DATES', 'GUSTAVO GUANABARA',
           'CELULAR', 'PYTHON')
for c in palavra:
    print(f'\nNa palavra {c} temos as vogais: ', end='')
    for l in c:
        if l in 'AEIOU':
            print(l, end=' | ')

