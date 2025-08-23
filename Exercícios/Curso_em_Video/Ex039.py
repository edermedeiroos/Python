# Faça um programa que leia o ano de nascimento de um jovem, e informe de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de ele se alistar
# Se ele ja passou do tempo de alistamento
# Seu programa também deve apresentar o tempo que falta ou passou do prazo
from datetime import date
print('ALISTAMENTO MILITAR')
print()
print('*'*50)
print()
nas = int(input('Ano de nascimento: '))
atual = date.today().year
print()
print('\033[1;034mCALCULANDO...\033[m')
print()
if nas > int(atual-18):
    print('Menor de 18 anos | \033[1;032mALISTAMENTO NÃO REQUERIDO\033[m | Faltam {} anos para seu alistamento'.format(18-(atual-nas)))
elif nas < int(atual-18):
    print('Maior de 18 anos | \033[1;031mALISTAMENTO REQUERIDO COM ATRASO\033[m | Passaram {} anos do seu alistamento'.format(atual-(nas+18)))
else:
    print('18 anos | \033[1;031mALISTAMENTO REQUERIDO\033[m')
