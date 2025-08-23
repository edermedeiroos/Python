# Crie um módulo chamado moeda.py que tenha as funções incorporadas:
# aumentar() | diminuir() | dobro() | metade()
# Crie também um programa que importe este módulo e execute essas funções
from Módulos.Utilidades import moeda
print('CALCULO DE PREÇO | MÓDULOS')
print()
print('-'*50)
print()
preco = float(input('Valor do produto: '))
print('-='*25)
print(f'• O dobro de R${preco} é R${moeda.dobro(preco, False)}')
print(f'• A metade de R${preco} é R${moeda.metade(preco, False)}')
print(f'• Aumentando 20% do R${preco} temos R${moeda.aumentar(preco, 20, False)}')
print(f'• Diminuindo 20% do R${preco} temos R${moeda.diminuir(preco, 20, False)}')
