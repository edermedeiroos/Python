# Faça um programa que tenha um função chamada ficha(), que receba dois parâmetros opcionais:
# O nome de um jogador e quantos gols ele marcou
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente
def ficha(jogador='<desconhecido>', gols='0'):
    print(f'O jogador {jogador} fez {gols} gols no campeonato.')


print('FICHA DE JOGADOR | FUNÇÃO')
print()
print('-'*50)
print()
jog = str(input('Nome do jogador: ')).strip()
ngol = str(input('Número de gols no campeonato: ')).strip()
if jog in '':
    if ngol in '':
        ficha()
    else:
        ficha(gols=ngol)
elif ngol in '':
    if jog in '':
        ficha()
    else:
        ficha(jogador=jog)
else:
    ficha(jog, ngol)

