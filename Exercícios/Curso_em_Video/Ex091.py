# Crie um programa onde 4 jogadores joguem um dado, e gere resultados aleatórios
# Guarde estes resultados em um dicionário. No final, coloque este dicionário em ordem
# O jogador que tirar o maior número vence
print('DADOS | DICIONÁRIO')
print()
print('*'*50)
print()
from random import randint
from operator import itemgetter
num = dict()
for c in range(1, 5):
    num[f'jogador{c}'] = randint(1, 6)
for i, k in num.items():
    print(f'{i} tirou {k}')
print('-='*25)
print(f'{"RANKING DOS JOGADORES":^50}')
print()
ranking = sorted(num.items(), key=itemgetter(1), reverse=True)
for i, k in ranking:
    print(f'{i} com {k}')