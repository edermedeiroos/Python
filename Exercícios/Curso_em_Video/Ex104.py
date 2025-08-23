# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ao input()
# Mas só faz a validação para aceitar valores númericos e que mostre um erro caso contrário
def leiaint(num):
    print(num, end='')
    num = input()
    while num.isalpha():
        print('\033[1:031mERRO | DIGITE UM NÚMERO INTEIRO VÁLIDO\033[m')
        num = input('Digíte um número: ')
        if num.isnumeric():
            return num
    return num


n = leiaint('Digíte um número: ')
print('-='*25)
print(f'Você digitou o número {n}')
