# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108
from Módulos.Utilidades import moeda
print('CALCULO DE PREÇO FORMATAÇÂO | MÓDULOS')
print()
print('-'*50)
print()
p = float(input('Valor do produto: '))
print('-='*25)
print(f'• O dobro de {moeda.moeda(p)} é {moeda.dobro(p)}')
print(f'• A metade de {moeda.moeda(p)} é {moeda.metade(p)}')
print(f'• Aumentando 20% do {moeda.moeda(p)} temos {moeda.aumentar(p, 20)}')
print(f'• Diminuindo 20% do {moeda.moeda(p)} temos {moeda.diminuir(p, 20)}')
