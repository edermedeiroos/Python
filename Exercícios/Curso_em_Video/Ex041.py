# A confederação nacional de natação quer um programa que leia o ano de nascimento de um atléta
# e mostre sua categoria de acordo com sua idade:
# Até 9 anos = MIRIM | Até 14 anos = INFANTIL | Até 19 anos = JUNIOR | Até 20 anos = SÊNIOR | Acima = MASTER
import datetime
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO - CATEGORIAS')
print()
print('*'*50)
print()
nas = int(input('Ano de nascimento: '))
idade = int(datetime.date.today().year) - nas
print()
if idade <= 9:
    print('O atleta tem {} anos | Categoria - \033[1;30mMIRIM\033[m'.format(idade))
elif 9 < idade <= 14:
    print('O atleta tem {} anos | Categoria - \033[1;31mINFANTIL\033[m'.format(idade))
elif 14 < idade <= 19:
    print('O atleta tem {} anos | Categoria - \033[1;32mJUNIOR\033[m'.format(idade))
elif idade == 20:
    print('O atleta tem {} anos | Categoria - \033[1;33mSÊNIOR\033[m'.format(idade))
else:
    print('O atleta tem {} anos | Categoria - \033[1;34mMASTER\033[m'.format(idade))
