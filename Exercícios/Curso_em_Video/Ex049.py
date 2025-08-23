# Refaça o exercício 9, mostrando a tabuada de um número que o usúario escolher
# utilizando o laço for
print('TABUADA')
print()
print('*'*50)
print()
n = int(input('Digite um número para ver sua tabuada: '))
print('_' * 12)
for p in range(1,11):
    print(n, 'x', p, '=', n*p)
print('_' * 12)