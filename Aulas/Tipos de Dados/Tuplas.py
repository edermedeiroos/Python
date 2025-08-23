# TUPLAS
# Tuplas são um conjunto de váriaveis
# Tuplas são imutáveis
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Sorvete')
print(lanche)
print(lanche[3])
print(lanche[0:3])
print(lanche[-1])
print(sorted(lanche))
print()
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print()
lanche.index('Suco')  # Serve para localizar o termo entre parênteses
lanche.count('Suco')  # Serve para contar o número de termos entre parênteses