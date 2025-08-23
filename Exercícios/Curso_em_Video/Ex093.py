# Crie um programa que gerencie o aproveitamento de um jogador de futebol
# O programa vai ler o nome do jogador e quantas partidas ele jogou
# Depois vai ler a quantidade de gols feitos em cada partida
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato
print('APROVEITAMENTO JOGADOR DE FUTEBOL')
print()
print('*'*50)
print()
cadastro = dict()
gols = []
cadastro['Nome'] = str(input('Nome do jogador: '))
cadastro['Partidas'] = int(input('Número de partidas jogadas: '))
print('-'*50)
cont = 0
somagols = 0
while cont != cadastro['Partidas']:
    cont += 1
    gols.append(int(input(f'Número de gols feitos na partida {cont}: ')))
    cadastro['Gols'] = gols
    somagols += gols[-1]
cadastro['Total'] = somagols
print('-='*25)
print(f'{"•APROVEITAMENTO•":^42}\n')
for p in range(0, cadastro['Partidas']):
    print(f'   - Na partida {p + 1} o jogador {cadastro["Nome"]} fez {gols[p]}')
print(f'\nTOTAL DE {somagols} gols')
