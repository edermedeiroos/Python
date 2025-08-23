# Faça um programa que mostre a tabuada de vários números, um de cada vez para cada valor digitado pelo usúario
# O programa será interrompido quando o valor digitado for negativo
print('TABUADA | BREAK')
print()
print('*'*50)
print()
n = int(input('Digíte um número para ver sua tabuada: '))
while True:
    if n < 0:
        break
    else:
        print('-'*30)
        for c in range(1, 11):
            print(c, 'x', n, '=', c*n)
        print('-'*30)
        n = int(input('Digíte um número para ver sua tabuada: '))
print()
print('--------------------------- PROGRAMA ENCERRADO ---------------------------')
