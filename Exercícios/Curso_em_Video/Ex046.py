# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício
# indo de 10 até 0 com uma pausa de 1 segundo
import time
print('FOGOS DE ARTIFÍCIO')
print()
print('*'*50)
print()
print('Fogos em:')
for cont in range(10, 0, -1):
    print(cont)
    time.sleep(1)
print()
print('FELIZ ANO NOVO!!!')