# Crie um programa que leia duas notas e calcule sua média, e mostre uma mensagem no final de acordo com a média
# Média abaixo de 5.0 = Reprovado | Média entre 5.0 e 6.9 = Recuperação | Média 7.0 ou superio = Aprovado
print('MÉDIA ESCOLAR')
print()
print('*'*50)
print()
n1 = float(input('Valor da primeira nota: '))
n2 = float(input('Valor da segunda nota: '))
print()
m = (n1+n2) / 2
if m < 5:
    print('Suas notas resultaram numa média {} | Status: \033[1;31mREPROVADO\033[m'.format(m))
elif 5 <= m < 7:
    print('Suas notas resultaram numa média {} | Status: \033[1;33mRECUPERAÇÃO\033[m'.format(m))
else:
    print('Suas notas resultaram numa média {} | Status: \033[1;32mAPROVADO\033[m'.format(m))