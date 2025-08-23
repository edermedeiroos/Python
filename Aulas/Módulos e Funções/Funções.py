# Podemos definir novos comandos atrávez das funções utilizando o def
from time import sleep


def linha():
    print('-'*50)


linha()
print('Karalho função é mt pika pprt tmj')
linha()

# Podemos também adicionar um parâmetro entre os parênteses


def mensagem(msg):
    print('-'*50)
    print(msg)


mensagem('Olha isso que foda pprt q dlc')
mensagem('HAHAHAHHA')
mensagem('Ai como isso é pika')


def soma(a, b):
    s = a + b
    print(s)


soma(10, 24)
soma(8, 9)
soma(32554, 734)

# Utilizamos o * junto de parâmetros para empacota-los todos em um só


def contador(* num):
    for valor in num:
        print(valor, '| ', end='')


contador(2, 1, 9)
contador(3, 10, 43)
contador(0, 57, 93, 85, 92)
print()

# Podemos acessar as diversas funcionalidade através da função help()

help(print)
help(input)
print(input.__doc__)

# Para utilizarmos o help com funções próprias utilizamos os docstrings


def contador(i, f, p):
    """Faz uma contagem e mostra na tela
    :parameter i: início da contagem
    :parameter f: fim da contagem
    :parameter p: passo da contagem
    :return: sem retorno"""
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


help(contador)

# Para deixarmos um parâmetro opcional nas defs utilizamos na frente do parâmetero o =
# O problema de parâmetros opcionais é que se o parâmetro for um tipo de dado mutável, sempre que executarmos a função utilizando o parametro opcional, ela utilizara o 
# mesmo dado mutável utilizado anteriormente


def somar(a=0, b=0, c=0):
    """Faz a soma dos 3 parâmetros"""
    s = a + b + c
    print(f'A soma vale {s}')


somar(4, 8, 10)
somar(a=3, c=9)
somar(3, 8)

# O escopo faz referência a qual parte do código ela está escrita


def teste(b):
    global a  # Ao colocarmos o global na frente de uma váriavel atribuimos o valor externo
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste(a)
print(f'A fora vale {a}')

# Para retornarmos valores de funções á variáveis utilizamos o return


def subtrair(d=0, e=0, f=0):
    sub = d - e - f
    return sub


r1 = subtrair(95, 64, 15)
r2 = subtrair(65, 90)
r3 = subtrair(81)
print(f'Os resultados foram {r1}, {r2} e {r3}')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('É ímpar!')

# Positional-Only Parameters (/) e Keyword-Only Arguments (*)
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# Positional-only Parameters (/) - Tudo antes da barra deve ser APENAS posicional.
# Keyword-Only Arguments (*) - Tudo depois do asterisco deve ser APENAS nomeado.

def soma(a, b, /, *, c, **kwargs):
    print(kwargs)
    print(a + b + c)


soma(1, 2, c=3, nome='teste')