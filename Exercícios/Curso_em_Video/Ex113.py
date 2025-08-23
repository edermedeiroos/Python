# Reescreva a função leiaint() que fizemos no desafio 104, incluindo agora a possibilidade de digitação de um número
# de tipo inválido. Aproveite e crie também a função leiafloat com a mesma funcionalidade
def leiaint(msg):
    while True:
        print(msg, end='')
        try:
            num = int(input())
        except (ValueError, TypeError):
            print('\033[031m • ERRO | Tipo de dado inserido inválido!\033[m')
        except KeyboardInterrupt:
            print('\033[031m • ERRO | Digitação interrompida!\033[m')
            return 0
        else:
            print('-='*25)
            print(f'    • O valor inteiro digitado foi {num}\n')
            break


def leiafloat(msg):
    while True:
        print(msg, end='')
        try:
            num = float(input())
        except (ValueError, TypeError):
            print('\033[031m • ERRO | Tipo de dado inserido inválido!\033[m')
        except KeyboardInterrupt:
            print('\033[031m • ERRO | Digitação interrompida!\033[m')
            return 0
        else:
            print('-='*25)
            print(f'    • O valor real digitado foi {num}\n')
            break


leiaint('Dígite um número inteiro: ')
leiafloat('Digíte um número real: ')
