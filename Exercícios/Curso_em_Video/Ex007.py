# Desenvolva um programa que leia as duas notas de um aluno
# e calcule e mostre sua média
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = n1*(1/2) + n2*(1/2)
print ('A média das suas notas {}, e {} é {}.' .format (n1, n2, m))