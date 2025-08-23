# Faça um programa que jogue par ou ímpar com o computador
# O jogo será interrompido quando o jogador perder, mostrando no final o número de vitórias consecutivas
from random import randint
print('PAR OU ÍMPAR')
print()
print('*'*50)
print()
print(' - Vamos jogar par ou ímpar!!!')
print()
njogador = int(input('Diga um valor: '))
jogador = input('Sua jogada [P/I]: ').strip().upper()
pc = randint(1, 10)
acerto = 0
while True:
    if (njogador + pc) % 2 == 0:
        print('Sua jogada: {}'.format(njogador))
        print('Minha jogada: {}'.format(pc))
        print()
        print('{} + {} = {} | PAR'.format(njogador, pc, njogador + pc))
        if jogador in 'P':
            print()
            print('VOCÊ GANHOU!!!')
            print('Vamos jogar novamente...')
            acerto += 1
            njogador = int(input('Diga um valor: '))
            jogador = input('Sua jogada [P/I]: ').strip().upper()
            pc = randint(1, 10)
        else:
            print()
            print('VOCÊ PERDEU!!!')
            break
    else:
        print('Sua jogada: {}'.format(njogador))
        print('Minha jogada: {}'.format(pc))
        print()
        print('{} + {} = {} |ÍMPAR'.format(njogador, pc, njogador + pc))
        if jogador in 'I':
            print()
            print('VOCÊ GANHOU!!!')
            print('Vamos jogar novamente...')
            acerto += 1
            njogador = int(input('Diga um valor: '))
            jogador = input('Sua jogada [P/I]: ').strip().upper()
            pc = randint(1, 10)
        else:
            print()
            print('VOCÊ PERDEU!!!')
            break
print()
print('GAME OVER | Você fez {} acertos'.format(acerto))
