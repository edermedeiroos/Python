# Faça um programa que tenha uma função chamada área(), que receba as dimensões
# de um terreno retangular (largura e comprimento) e mostre a área do retângulo
print('AREA DO RETÂNGULO | FUNÇÕES')
print()
print('*'*50)
print()


def area(a, b):
    ar = a*b
    print()
    print(f'A área do retângulo {a} x {b} é: {ar}')


area(float(input('Altura do objeto: ')), float(input('Largura do objeto: ')))
