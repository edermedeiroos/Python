# ESTRUTURA DE REPETIÇÃO FOR
# Utilizamos for para repetir um mesmo comando num determinado range(intervalo)
# Dentro do range temos 3 valores, o primeiro onde começa a repetição, o segundo aonde termina,
# E o terceiro de quantos em quantos será pulado

print('ESTRUTURA DE REPETIÇÃO FOR')
s = 0
for c in range(0, 10, 2):
    n = int(input('Digite um valor: '))
    s += n
print('A soma dos valores é {}'.format(s))