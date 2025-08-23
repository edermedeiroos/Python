# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
# A multa vai custar R$7,00 para cada km acima do limite.
v = float(input('Digíte a velocidade do carro: '))
if v>80:
    print('Você ultrapassou o limite de velocidade.\nO valor da multa é: R${:.2f}'.format((v-80)*7))
else:
    print('Você estava dentro do limite de velocidade, não sera multado.')
