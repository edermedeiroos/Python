# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dólares ela pode comprar.
# Considere US$ = 3,27
din = float(input('Quantos reais você tem na carteira ?'))
dol = float(din/3.27)
print('Com os seus {} reais, você pode comprar {} dólares.' .format(din, dol))