# Faça um programa, que ajudo um jogador da mega-sena a criar palpites.
# O programa deve perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
# para cada jogo cadastrando tudo em uma lista composta
from random import randint
from time import sleep
print('MEGA-SENA')
print()
print('*'*50)
print()
jog = int(input('Quantas jogadas deseja fazer? '))
lista = []
listatemp = []
cont = 0
for c in range(0, jog):
    while cont != 6:
        n = randint(0, 60)
        if n not in listatemp:
            listatemp.append(n)
            cont += 1
    lista.append(listatemp[:])
    listatemp.clear()
    cont = 0
print()
for e in range(0, jog):
    print(f'Jogada {e + 1}: {sorted(lista[e])}')
    print('-'*50)
    sleep(0.5)
print(' '*17, ' BOA SORTE ', ' '*17)
