# Aprimore o desafio 93 para que ele funcione com vários jogadores
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
print('APROVEITAMENTO JOGADORES DE FUTEBOL')
print()
print('*'*50)
print()
time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas o jogador *{jogador["nome"]}* jogou? '))
    print()
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'   • Gols na partida {c + 1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    print()
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ARGUMENTO INVÁLIDO')
    print('-'*50)
    if resp in 'N':
        break

print('-=' * 25)
print(f'{"•APROVEITAMENTO•":^42}\n')
print(f'{"No.":<3}{"NOME":<20}{"GOLS":<20}{"TOTAL":<20}')
for k, v in enumerate(time):
    print(f'{k:<3}', end='')
    for d in v.values():
        print(f'{str(d):<20}', end='')
    print()
print()
while True:
    busca = int(input('Mostrar dados de qual jogador ? [999 encerra] '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print()
        print(f'--- LEVANTAMENTO | {time[busca]["nome"].upper()} ---\n')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    • No jogo {i + 1} fez {g} gols.')
    print('-'*50)
print()
print(f'{"PROGRAMA ENCERRADO":^50}')
