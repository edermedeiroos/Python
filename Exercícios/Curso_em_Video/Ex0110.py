# Adicione ao módulo moeda.py criado nos desafios anteriores uma função chamada resumo()
# que mostra na tela algumas informações geradas pelas funções que ja temos no módulo criado até aqui
from Módulos.Utilidades import moeda
print('FUNÇÃO RESUMO | MÓDULOS')
print()
print('-'*50)
print()
preco = float(input('Valor do produto: '))
aumento = float(input('Aumento hipotético: '))
diminuir = float(input('Diminuição hipotética: '))
print('-'*50)
moeda.resumo(preco, aumento, diminuir)
