# Elabore um programa que calcule um valor a ser pago por um produto, considerando a forma de pagamento:
# À vista dinheiro/cheque = 10% de desconto | À vista no cartão: 5% de desconto
# Em até 2x no cartão = preço normal | 3x ou mais no cartão = 20% de juros
print('PREÇO')
print()
print('*'*50)
print()
p = float(input('Digíte o valor do produto: R$'))
print()
print('Formas de pagamento:\n[ 0 ] = À vista dinheiro/cheque\n[ 1 ] = À vista cartão', end='')
print('\n[ 2 ] = Até 2x no cartão\n[ 3 ] = 3x ou mais no cartão')
print()
f = int(input('Digíte a forma de pagamento: '))
if f == 0:
    print('Seu produto terá 10% de desconto!!! - Valor final: R${}'.format(p - p/10))
elif f == 1:
    print('Seu produto terá 5% de desconto!!! - Valor final: R${}'.format(p - p/20))
elif f == 2:
    print('Seu produto não é válido a descontos. - Valor final: R${}'.format(p))
elif f == 3:
        pc = int(input('Número de parcelas: '))
        print()
        print('Seu produto parcelado em {} vezes terá 20% de juros. - Valor final: R${}'.format(pc, p + p / 5))
else:
    print('Escolha uma forma de pagamento válida.')
