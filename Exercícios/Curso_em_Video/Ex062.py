# Melhore o desafio 61, perguntando se o úsuario quer mostrar mais termos
# o programa para quando o úsuario digitar 0 termos
print('PROGRESÃO ARITIMÉTICA | WHILE | INTERAÇÃO COM O USÚARIO')
print()
print('*'*50)
print()
pt = int(input('Dígite o primeiro termo da P.A: '))
r = int(input('Digíte a razão da progressão: '))
print()
cont = -1
dt = pt
while cont < 9:
    cont += 1
    dt = pt + r*cont
    print(dt, end=' | ')
print()
dt2 = pt
cont2 = 0
cont3 = 0
mais = int(input('Deseja exibir mais quantos termos ? [0] para sair: '))
while mais != 0:
    while cont2 < mais:
        cont += 1
        cont2 += 1
        cont3 += 1
        dt2 = dt + r*cont3
        print(dt2, end=' | ')
    print()
    cont2 = 0
    mais = int(input('Deseja exibir mais quantos termos ? [0] para sair: '))
print()
print('O número total de termos exibidos foram {}'.format(cont + 1))
print()
print('----------------------------------- PROGRAMA ENCERRADO -----------------------------------')
