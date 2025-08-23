# Faça um programa que calcule a soma de todos os números ímpares que são multíplos de 3
# e que se encontram num intervalo de 1 até 500
print('SOMA DE ÍMPARES')
print()
print('*'*50)
print()
soma = 0
nums = 0
for s in range(1, 501):
    if s % 3 == 0 and s % 2 != 0:
        nums = nums + 1
        soma = soma + s
print('A soma dos {} números ímpares e multiplos de 3 no intervalo de 1 à 500 é: {}'.format(nums, soma))

