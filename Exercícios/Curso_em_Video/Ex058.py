# Melhore o jogo do desafio 28, só que agora, o jogador vai tentar adivinhar até acertar
# mostrando no final quantos palpites foram usados
import random
n = (random.randint(0, 5))
print('Acabei de pensar num número de 0-5')
jog = int(input('Tente adivinha-lo!!! '))
palpite = 0
while n != jog:
    print()
    print('HAHAHAHA VOCÊ ERROU!!! O NÚMERO QUE EU PENSEI FOI {}'.format(n))
    print()
    palpite += 1
    n = (random.randint(0, 5))
    jog = int(input('Tente novamente: '))
print()
print('VOCÊ ACERTOU!!!')
print()
print('Você fez {} palpites.'.format(palpite))