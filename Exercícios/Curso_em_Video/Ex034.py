# Escreva um programa que leia o salário de um funcionário e mostre o valor do seu aumento
# Para salários superiores à R$1250.00, calcule um aumento de 10%
# Para salários inferiores ou iguais à R$1250.00, calcule um aumento de 15%
sal = float(input('Dígite seu salário para saber o aumento: R$'))
print()
print('-'*50)
print()
if sal>1250.00:
    print('Seu novo salário com 10% de aumento será equivalente à: R${}'.format(sal+sal/10))
else:
    print('Seu novo salário com 15% de aumento será equivalente à: R${}'.format(sal+sal/100*15))