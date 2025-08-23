# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário
# Se por acaso a CTPS for diferente de zero o dicionário receberá também o ano de contratação e o salário
# Calcule e acrescente além da idade, com quantos anos a pessoa vai se aposentar.
# Considere a aposentadoria como 35 anos de contribuição
from datetime import datetime
print('CARTEIRA DE TRABALHO')
print()
print('*'*50)
print()
cadastro = dict()
cadastro['Nome'] = str(input('Nome do trabalhador: '))
cadastro['Nascimento'] = int(input('Ano de nascimento: '))
cadastro['Idade'] = datetime.today().year - cadastro['Nascimento']
cadastro['CTPS'] = int(input('Carteira de trabalho [0 não tem]: '))
if cadastro['CTPS'] != 0:
    cadastro['Contratação'] = int(input('Ano de contratação: '))
    cadastro['Salário'] = float(input('Salário: '))
    aposentar = (cadastro['Contratação'] + 35) - cadastro['Nascimento']
    cadastro['Aposentadoria'] = aposentar
    print()
    print('-='*25)
    for k, i in cadastro.items():
        print(f'O campo {k} tem valor {i}')
    print('-='*25)
    if datetime.today().year - cadastro['Nascimento'] >= aposentar:
        print('VOÇÊ JÁ PODE APOSENTAR!!!')
    else:
        print('Voçê ainda não pode aposentar :(')
else:
    print('-='*25)
    for k, i in cadastro.items():
        print(f'O campo {k} tem valor {i}')
    print('-=' * 25)
    print('Voçê ainda não pode aposentar :(')
