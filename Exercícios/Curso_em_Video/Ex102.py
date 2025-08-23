# Crie um programa, que tenha uma função chamada fatorial() que receba dois parâmetros:
# O primeiro que indique o número a calcular e o segundo chamado show, que será o valor lógico(opcional)
# Indicando se será mostrado ou não o calculo na tela
def fatorial(n, show):
    fatorado = 1
    for c in range(n, 0, -1):
        fatorado *= c
        if show in 'S':
            if c == 1:
                print(c, end='')
            else:
                print(f'{c} x ', end='')
    if show in 'S':
        print(f' = {fatorado}')
    else:
        print(f'{n}! = {fatorado}')


print('FATORIAL | FUNÇÃO')
print()
print('-'*50)
print()
num = int(input('Digite o númeroo a ser fatoriado: '))
mostra = str(input('    • Deseja mostrar o calculo? ')).strip().upper()[0]
print()
fatorial(num, mostra)
