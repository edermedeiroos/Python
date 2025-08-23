# Adapte o código do exercício 107 criando uma função adicional chamada moeda()
# que consiga mostrar os valores como um valor monetário formatado
from Módulos.Utilidades import moeda
print('CALCULO DE PREÇO FORMATAÇÂO | MÓDULOS')
print()
print('-'*50)
print()
p = float(input('Valor do produto: '))
print('-='*25)
print(f'• O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'• A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'• Aumentando 20% do {moeda.moeda(p)} temos {moeda.moeda(moeda.aumentar(p, 20))}')
print(f'• Diminuindo 20% do {moeda.moeda(p)} temos {moeda.moeda(moeda.diminuir(p, 20))}')