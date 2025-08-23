# Faça um programa que tenha um função chamada escreva(), que receba um texto qualquer como parâmetro
# e mostre a mensagem com tamanho adaptável
print('TAMANHO ADAPTÁVEL')
print()
print('-'*50)
print()


def escreva(text):
    tamanho = len(text) + 6
    print()
    print('-'*tamanho)
    print(f'   {text}   ')
    print('-'*tamanho)


escreva(str(input('Escreva uma mensagem: ')))
