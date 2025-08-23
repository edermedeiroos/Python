# Crie um programa que faça o computado jogar JOKENPÔ com você
import random
import time
import emoji
print('JOKENPÔ')
print()
print('*'*50)
print()
print('- Vamos jogar Jokenpô!!!')
print('Suas opções:\n[ 1 ] = Pedra\n[ 2 ] = Papel\n[ 3 ] = Tesoura')
print()
print('Vou contar até 3, após isso, faça sua jogada!!!')

time.sleep(1)
print('1')
time.sleep(1)
print('2')
time.sleep(1)
print('3 !!!')
jogador = int(input('JOGUE!!!: '))
pc = random.randint(1, 3)
print()
if jogador == 1:
    print(emoji.emojize('Sua jogada: :luggage:'))
elif jogador == 2:
    print(emoji.emojize('Sua jogada: :page_facing_up:'))
elif jogador == 3:
    print(emoji.emojize('Sua jogada: :scissors:'))
print('     VS     ')
if pc == 1:
    print(emoji.emojize('Minha jogada: :luggage:'))
elif pc == 2:
    print(emoji.emojize('Minha Jogada: :page_facing_up:'))
elif pc == 3:
    print(emoji.emojize('Minha jogada: :scissors:'))
print()
if (jogador == 1 and pc == 3) or (jogador == 2 and pc == 1) or (jogador == 3 and pc == 2):
    print('IMPOSSÍVEL. COMO VOCÊ GANHOU DE MIM?!?!?!?!?')
elif (jogador == 3 and pc == 1) or (jogador == 1 and pc == 2) or (jogador == 2 and pc == 3):
    print('HAHAHAHAHAHAHA, É ÓBVIO QUE EU GANHEI!!!!')
elif jogador == pc:
    print('EMPATAMOS!')
