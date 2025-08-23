# Crie uma função que encontra o primeiro duplicado considerando o segundo
# número como a duplicação. Retorne a duplicação considerada.
# Requisitos:
#    A ordem do número duplicado é considerada a partir da segunda
#    ocorrência do número, ou seja, o número duplicado em si.
#    Exemplo:
#        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
#        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
#        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
#    Se não encontrar duplicados na lista, retorne -1

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def duplicado(lista):
    repetidos = []
    for n in lista:
        if lista.count(n) > list(set(lista)).count(n): # Verifica se há números duplicados
            repetidos.append(n) # Se tiver, adiciona-o na lista de repetidos
    
    segunda_ocorrencia = []
    for n in repetidos:
        if n in segunda_ocorrencia: # Verifica se o numero repetido ja foi verificado antes
            return n # Se estiver, retorna o número
        segunda_ocorrencia.append(n)
    
    return -1 # Se não houver números repetidos, retorna -1

for lista in lista_de_listas_de_inteiros:
    print(f'• LISTA: {lista}\n')
    qual_valor = duplicado(lista)
    if qual_valor > 0: # Se houver duplicados, exibe o número com a segunda ocorrencia repetida
        print(f'O valor duplicado a partir da segunda ocorrência é: {qual_valor}')
    else: # Se não houver duplicados
        print(f'Não encontramos valores duplicados nesta lista')
    print('-'*50)
