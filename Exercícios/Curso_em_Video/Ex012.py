# Faça um algoritmo que leia o preço de um produto e mostre seu
# novo preço, com 5% de desconto.
p = float(input('Digite o preço do produto'))
pd = p - (p/100 * 5)
print('O preço do produto com com 5% de desconto é {}.'.format (pd))
