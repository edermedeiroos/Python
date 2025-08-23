# Crie um programa que aprove um empréstimo bancário para compra de uma casa
# O programa precisa perguntar o valor da casa, o salário do comprador, e em quantos anos ele vai pagar
# Calcule o valor da prestação mensal sabendo q ela n pode exceder 30% do salário
# ou então o empréstimo será negado
print('APROVAÇÃO DE EMPRÉSTIMO')
print()
print('*'*50)
print()
val = float(input('Valor do imóvel: R$'))
sal = float(input('Salário do comprador: R$'))
anos = float(input('Anos de pagamento: '))
print()
pm = val/(anos*12)
if pm > sal*0.3:
    print('A prestação mensal(R${:.2f}) é superior à 30% do seu salário | \033[1;31mEMPRÉSTIMO NEGADO\033[m'.format(pm))
else:
    print('A prestação mensal(R${:.2f}) é inferior à 30% do seu salário | \033[1;32mEMPRÉSTIMO APROVADO\033[m'.format(pm))
