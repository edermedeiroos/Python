# Refaça o exercício 51, lendo o primeiro termo e a razão da P.A, mostrando os 10 primeiros termos
# da progressão usando a estrutura while
print('PROGRESÃO ARITIMÉTICA | WHILE')
print()
print('*'*50)
print()
pt = int(input('Dígite o primeiro termo da P.A: '))
r = int(input('Digíte a razão da progressão: '))
print()
cont = 0
dt = pt
while cont < 9:
    cont += 1
    dt = pt + r*cont
    print(dt, end=' | ')
print()
print('O 10 termo é {}'.format(dt))
