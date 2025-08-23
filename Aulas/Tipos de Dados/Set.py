# SETS - CONJUNTOS EM PYTHON (tipo set)
# Sets em Python são mutáveis, porém aceitam apenas tipos imutáveis como valor interno.
# Criando um set: set(iterável) ou {1, 2, 3}

set1 = set('Eder')
set1 = set()  # Set vazio
set1 = set({'Eder', 1, 2, 3})  # Set com dados

# Sets são eficientes para remover valores duplicados de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

l1 = [1, 2, 3, 3, 3, 3, 3, 1]
set1 = set(l1)
print(set1)
print(3 not in set1)
for numero in set1:
     print(numero)

# Métodos úteis:
# add - Adiciona um valor ao set [Só um por vez]
# update - Adiciona vários valores ao set 
# clear - limpa o set inteiro
# discard - limpa um valor específico do set

set1 = set()
set1.add('Eder')
set1.update('Olá Mundo') # Adicionara cada letra como um valor
set1.update(('Olá Mundo', 1, 2, 3, 4)) # Adicionara cada item dentro da tupla como um valor único
set1.clear()
set1.discard('Olá Mundo')
set1.discard('Eder')
print(set1)

# Operadores úteis:
# Utilizamos o símbolo '|' ou union() - Une dois sets
# Utilizamos o símbolo '&' ou intersection() - Itens presentes em ambos
# Utilizamos o símbolo '-' ou difference() - Itens presentes apenas no set da esquerda
# Utilizamos o símbolo '^' ou symmetric_diference() - Itens que não estão em ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s1 - s2
s3 = s1 ^ s2

# SET COMPREHENSION
# Forma de criar sets a partir de iteráveis

s1 = {2 ** i for i in range(10)} # s1 = 2 elevado ao iteravel no range(10)
print(s1)
