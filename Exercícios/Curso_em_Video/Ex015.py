# Escreva um programa que pergunte a quantidade de quilometros
# percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o
# carro custa R$60 por dia e R$0,15 por km rodado.
d = int(input('Dias alugado: '))
k = float(input('Km rodados: '))
p = (d*60) + (k*0.15)

print('O carro alugado por {} dias, e percorrido por {}km, terá um preço final de {}.'.format(d, k, p))