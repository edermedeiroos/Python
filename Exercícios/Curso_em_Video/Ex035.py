# Crie um programa que leia o comprimento de 3 retas, e diga se ele pode ou não formar um triângulo
r1 = float(input('Valor da reta 1: '))
r2 = float(input('Valor da reta 2: '))
r3 = float(input('Valor da reta 3: '))
print()
if r1 + r2 <= r3 or r1 + r3 <= r2 or r2 + r3 <= r1:
    print(' - É impossivel formar um triângulo com estas medidas')
else:
    print(' - É possivel formar um trinângulo com estas medidas')