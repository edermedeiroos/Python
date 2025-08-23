# Crie um programa que leia 2 valores, e mostre um menu na tela:
# [1] = soma | [2] = multiplicação | [3] = maior | [4] = novos números | [5] = sair do programa
# seu programa deverá realizaqr a operação solicitada em cada caso
print('MENU DE INTERAÇÃO')
print()
print('*'*50)
print()
v1 = int(input('Valor 1: '))
v2 = int(input('Valor 2: '))
print()
print('DIGÍTE: [1] = soma | [2] = multiplicação | [3] = maior | [4] = novos números | [5] = sair do programa')
print()
op = int(input('Escolha a operação: '))
while op != 5:
    if op == 1:
        print()
        print(v1, '+', v2, '=', v1 + v2)
        print()
        op = (int(input('Se deseja fazer outra operação digíte [4] | Se deseja sair do programa digíte [5]')))
    elif op == 2:
        print()
        print(v1, 'x', v2, '=', v1 * v2)
        print()
        op = (int(input('Se deseja fazer outra operação digíte [4] | Se deseja sair do programa digíte [5]')))
    elif op == 3:
        if v1 > v2:
            print()
            print(v1, '>', v2)
            print()
            op = (int(input('Se deseja fazer outra operação digíte [4] | Se deseja sair do programa digíte [5]')))
        elif v1 < v2:
            print()
            print(v1, '<', v2)
            print()
            op = (int(input('Se deseja fazer outra operação digíte [4] | Se deseja sair do programa digíte [5]')))
        else:
            print()
            print(v1, '=', v2)
            print()
            op = (int(input('Se deseja fazer outra operação digíte [4] | Se deseja sair do programa digíte [5]: ')))
    elif op == 4:
        print()
        v1 = int(input('Novo valor 1: '))
        v2 = int(input('Novo valor 2: '))
        op = int(input('Nova operação: '))
        print()
    else:
        op = int(input('Digíte uma operação válida: '))
print()
print('--- MENU FINALIZADO ---')
