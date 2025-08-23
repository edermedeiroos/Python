# Crie um programa que gera 5 números aleatórios e o coloque em uma tupla
# Depois disso, mostre os números, e também seu maior e menos
print('SORTEADOR | SUPLA')
print()
print('*'*50)
print()
import random
nums = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
print(f'Eu sorteei os números: {nums}')
print()
print(f'O maior valor sorteado foi {max(nums)}, e o menos {min(nums)}.')
print()
print('--------------------------------- PROGRAMA ENCERRADO ---------------------------------')
