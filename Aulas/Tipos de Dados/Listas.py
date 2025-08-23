# LISTAS
# Listas também são um conjunto de variáveis
# listas são mutáveis

num = list([4, 5, 18, 9])
num2 = list([8, 2, 5, 1])
num.append(8)  # adiciona uma variavel no final da lista
num.insert(2, 0)  # adiciona uma variavel em determina posição
del num[2]  # apaga determinada posição
num.pop(4)  # apaga determinada posição
num.remove(5)  # apaga determinado elemento
num.extend(num2)  # extende a lista com determinado argumento 
valores = list(range(4, 11))
valores.sort()  # organiza a lista por ordem numérica
valores.sort(reverse=True)  # organiza a lista por ordem numérica inversa
print(num)
valores2 = list()
valores2.append(5)
valores2.append(4)
valores2.append(9)
for cont in range(0, 7):
    valores2.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores2):
    print(f'Na posição {c + 1} encontrei o valor {v}!')
print('Cheguei ao final da lista')

d = list([1, 3, 6, 9])
e = d  # Caso adicionemos d[:], faremos uma copia da lista, fazendo com que elas sejão distintas
e[2] = 8
print(f'Lista D: {d}')
print(f'Lista E: {e}')
d = list([1, 3, 6, 9])
e = d[:]
print(e)

# LISTAS COMPOSTAS
# Podemos adicionar listas dentro de listas

pessoas = [['Pedro', 25], ['Maria', 18], ['Eder', 15], ['Giovana', 16]]
print(pessoas[0])
print(pessoas[0][0])
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade')
print()
teste = list()
teste.append('Eder')
teste.append(15)
galera = list()
galera.append(teste[:])  # Utilizamos [:] para fazer uma cópia
teste[0] = 'Giovana'
teste[1] = 16
galera.append(teste[:])
print(galera)
print()
galera2 = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Digite o nome: ')))
    dado.append(int(input('Digite a idade: ')))
    galera2.append(dado[:])
    dado.clear()
print()
print(galera2)

# LIST COMPREHENSION
# Forma rápida para criar listas a partir de iteráveis.

lista = []
for numero in range(10):
    lista.append(numero)

lista = [numero for numero in range(10)] # Adiciona o {numero} para cada {numero} no range(10)
# MAPEAMENTO - LIST COMPREHENSION
# Mudar os dados da lista sem alterar o tamanho

produtos = [
    {'nome': 'produto1', 'preco': 20, },
    {'nome': 'produto2', 'preco': 10, },
    {'nome': 'produto3', 'preco': 30, },
]
novos_produtos = [ 
    {**produto, 'preco': produto['preco'] * 1.05} # Desempacota o produto e aumenta o preço em 5% caso:
    if produto['preco'] > 20 else {**produto} # o preço do produto seja maior que 20, caso contrário o produto não sofre alteração
    for produto in produtos
]

# É possível mapear uma lista atravéz da função map(), tendo como argumentos uma função para alterar os valores do iteravel, e o iteravel que vai ser mudado

def aumenta10(produto):
    return {
        **produto, 'preco': produto['preco'] * 1.1 
    }

list(map(aumenta10, novos_produtos))

# FILTRO - LIST COMPREHENSION
# Filtro decide se determinado valor entra ou não na lista

lista = [n for n in range(10) if n < 5] # Adiciona o {numero} para cada {numero} no range(10) Se for menor que 5
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} # Desempacota o produto e aumenta o preço em 5% caso:
    if produto['preco'] > 20 else {**produto} # o preço do produto seja maior que 20, caso contrário o produto não sofre alteração
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10 # Adiciona o novo_produto na lista caso True nas condições
]

# É possível filtrar uma lista atravéz da função filter(), tendo como argumentos a condição do filtro, e o iteravel que vai ser mudado

func_filter = filter(lambda p: p['preco'] > 10, produtos) # Vai filtrar os valores dentro de produtos que possuem o 'preco' maior que 10 e adiciona-los na variável