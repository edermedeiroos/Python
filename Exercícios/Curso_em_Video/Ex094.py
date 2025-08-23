# Crie um programa que leia nome sexo e idade de várias pessoas guardando os dados de cada pessoa em
# um dicionário e todos os dicionários em uma lista. No final mostre:
# Quantas pessoas foram cadastradas | A média de idade do grupo | uma lista com todas as mulheres |
# Uma lista com todas as pessoas com idade acima da média.
print('UNINDO LISTAS E DICIONÁRIOS')
print()
print('*'*50)
print()
galera = []
pessoa = dict()
media = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    pessoa['Idade'] = int(input('Idade: '))
    pessoa['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    while pessoa['Sexo'] not in 'MF':
        pessoa['Sexo'] = str(input('Reposta inválida [F/M]: ')).strip().upper()
    media += pessoa['Idade']
    galera.append(pessoa.copy())
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
    print('-' * 50)
    while resp not in 'SN':
        resp = str(input('Reposta inválida [S/N]: ')).strip().upper()
    if resp in 'N':
        break
media = media / len(galera)
print(f'{"ESTATÍSTICAS":^50}\n')
print(f'• O número de pessoas cadastradas é {len(galera)}')
print(f'• A média de idade do grupo é: {media:.0f} anos ')
print(f'• As mulheres cadastradas foram:', end=' ')
for p in galera:
    if p['Sexo'] in 'F':
        print(p['Nome'], end=' | ')
print()
print(f'• A lista de pessoas com idade acima da média foram:', end=' ')
for p in galera:
    if p['Idade'] > media:
        print(p['Nome'], end=' | ')
print()
print(f'{"PROGRAMA ENCERRADO":^50}\n')

