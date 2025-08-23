# Faça um mini sistema que utilize o interactive help do Python
# O usúario vai digitar o comando e o manual vai aparecer. Quando o usúario digitar Fim o programa encerra
# Obs: use cores
def manual(funcao):
    from time import sleep
    print('\033[043m*'*47)
    print(f'    Exibindo manual | Builtin {funcao}...     ')
    print('*'*47)
    sleep(1)
    print(f'\033[7;40m', end='')
    help(funcao)
    print('\033[m', end='')
    print('\033[044m*'*47)
    print('          PyHelp3 - Dev|Eder.Medeiros          ')
    print('*'*47)


while True:
    escolha = str(input('\033[mInteractive Help Python3 | Qual função deseja exibir ? \033[m')).strip()
    if escolha in 'fimFIM':
        break
    manual(escolha)
print(f'\033[042m{"*"*150}\n{"Obrigado por utilizar o INTERACTIVE HELP PYTHON3 | Volte sempre!!!":^150}\n{"*"*150}')
