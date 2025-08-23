# ESTRUTURA DE REPETIÇÃO WHILE
# Utilizamos o while para uma repetição que não soubermos o range limite

c = 1
while c < 10:
    print(c)
    c += 1
print()
n = 0
while n != 10:
    n = int(input('Digite um valor: '))
print()
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
print('Fim')