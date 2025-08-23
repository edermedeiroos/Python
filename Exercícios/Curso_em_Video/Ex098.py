# Faça um programa que tenha uma função chamada contador(), que receba 3 parâmetros: início, fim e passo
# Seu programa tem que realizar 3 contagens atravéz da função criada:
# De 1 até 10, de um em um | De 10 até 0, de 2 em 2 | Uma contagem personalizada
from time import sleep
print('CONTAGEM PERSONALIZADA')
print()
print('-'*50)
print()


def contador(i, f, p):
    print('-'*50)
    print(f'Contagem de {i} até {f} de {p} em {p}:\n')
    if f > i:
        for c in range(i, f+1, p):
            print(c, end=' | ')
            sleep(0.2)
        print()
    if i > f:
        if p > 0:
            for c in range(i, f-1, -p):
                print(c, end=' | ')
                sleep(0.2)
        elif p < 0:
            for c in range(i, f-1, p):
                print(c, end=' | ')
                sleep(0.2)
        else:
            print('Passo = 0 | Contagem ineficiente')
        print()


contador(1, 10, 1)
contador(10, 0, 2)
print('-'*50)
print(f'{"Agora é sua vez de personalizar a contagem!!!":^50}\n')
ini = int(input('Início: '))
fim = int(input('Final: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)