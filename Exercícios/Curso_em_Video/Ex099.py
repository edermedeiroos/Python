# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior
print('MAIOR | FUNÇÃO')
print()
print('-'*50)
print()


def maior(valores):
    m = 0
    for valor in valores:
        if valor > m:
            m = valor
    print(f'• Analisando os valores {valores}')
    print(f'• Foram informados {len(lista)} valores')
    print(f'• O maior valor foi: {m}')


lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? ')).strip().upper()[0]
    print('-='*25)
    if resp not in 'S':
        break
maior(lista)
