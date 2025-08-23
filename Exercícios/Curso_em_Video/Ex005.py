# Faça um programa que leia um número inteiro,
# e mostre seu sucessor e anterior
n = int(input('Digite um número: '))
ant = int(n-1)
suc = int(n+1)
print ('analizando o número {}, seu antecessor sera {}, '.format (n, ant), end='')
print ('e seu sucessor será {}'.format(suc))