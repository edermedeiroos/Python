# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior | O segundo valor é maior | Não existe valor maior, os números são iguais.
print('COMPARADOR NUMÉRICO')
print()
print('*'*50)
print()
n1 = int(input('Digíte um número inteiro qualquer: '))
n2 = int(input('Digíte outro número inteiro qualquer: '))
if n1 > n2:
    print('\033[1;32mO primeiro valor é maior.\033[m')
elif n2 > n1:
    print('\033[1;32mO segundo valor é maior\033[m')
else:
    print('\033[1;31mNão existe valor maior, os números são iguais.\033[m')
