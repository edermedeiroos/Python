# Crie um pacote chamado utilidadesCeV que tenha dois modúlos internos chamados móedas e dado
# Transfira todas as funções utilizadas nos desafios 107 | 108 | 109 para o primeiro pacote e mantenha tudo funcionando
from Módulos.Utilidades import moeda, dado
p = float(input('Preço: '))
moeda.resumo(p, 15, 60)
