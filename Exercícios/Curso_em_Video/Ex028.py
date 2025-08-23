# Escreva um programa que faça o computador pensar um número entre 0 e 5
# e peça para o usúario tentar descobrir qual foi o número escolhido.
# O programa deverá dizer sse o usúario acertou ou errou
import random
import time
n = (random.randint(0, 5))
a = int(input('Tente adivinhar o número de 0-5 que eu pensei\nSua aposta: '))
print()
print('PROCESSANDO...')
time.sleep(2)
print()
if a == n:
    print('--- PARABÉNS, VOCÊ ACERTOU!!!')
else:
    print('--- HAHAHA, VOCÊ ERROU!!!')
