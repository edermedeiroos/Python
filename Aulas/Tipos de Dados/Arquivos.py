# CRIANDO ARQUIVOS
# Para criarmos e/ou gerenciarmos os arquivos utilizamos a função open()
# É necessário utilizar o 'arquivo'.close() após aberto
# with open abre o arquivo e o fecha depois do comando executado dentro do escopo | podemos utilizar o as para nomealo como variavel
# Modos da função: r (leitura) | w (escrita) | x (para criação) | a (escreve ao final) | b (binário) | t (modo texto) | + (leitura e escrita)
# ATENÇÃO: • Modo 'w' apaga o arquivo inteiro e o reescreve | O encoding utf-8 serve para definirmos os caractéres iguais para o arquivo txt

# MÉTODOS ÚTEIS
# write - Escreve no arquivo
# read - Lê o arquivo
# writelines - Escreve várias linhas (Iterável)
# seek - Move o cursor para determinada posição
# readline - Lê a linha de determinada posição
# readlines - Lê as linhas de uma posição a outra

# MÉTODOS ÚTEIS MÓDULO OS
# os.remove ou unlink - Apaga determinado arquivo
# os.rename - Renomeia ou move determinado arquivo

# MÉTODOS ÚTEIS MÓDULO JSON
# json.dump = Gera um arquivo .json
# json.load = Carrega um arquivo .json para uma váriavel

caminho_arquivo = 'C:\\Users\\Eder\\.vscode\\Python\\'
caminho_arquivo += 'Teste_Open().txt'

"""
arquivo = open(caminho_arquivo, 'w')
arquivo.close()
"""

with open(caminho_arquivo, 'w+', encoding='utf-8') as arquivo:
    arquivo.write('Giovana\n')
    arquivo.write('Muito\n')
    arquivo.writelines(
        ('Gostosa\n', 'Puta ', 'Que ', 'Pariu ')
    )

    arquivo.seek(0, 0)
    print(arquivo.read())

    arquivo.seek(0, 0)
    print(arquivo.readline(), end='') # Devido a quebra de linha dentro da string, utiliza o end='' para eliminar a quebra de linha automatica do print()
    print(arquivo.readline().strip()) # Devido a quebra de linha dentro da string, utiliza o strip() para eliminar a quebra de linha automatica do print()

    arquivo.seek(0, 0)
    for linha in arquivo.readlines():
        print(linha, end='')

from os import remove
remove(caminho_arquivo)

# ARQUIVOS .JSON (JavaScript Object Notation)
# Compacto banco de dados, muito similar aos dicionários em python

# MÉTODOS ÚTEIS MÓDULO JSON
# json.dump = Gera um arquivo .json
# json.load = Carrega um arquivo .json para uma váriavel

import json

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open('Arquivo_Json.json', 'w', encoding='utf8') as arquivo:
    json.dump(pessoa, # Passa a variavel para um arquivo.json | json.dumps faz o dump de uma string
               arquivo,
               ensure_ascii=False, # Adiciona os acentos e caractéres especiais ao json
               indent=2) # Formata o dicionário com escopos e tals
    
with open('Arquivo_Json.json', 'r', encoding='utf-8') as arquivo:
    pessoa = json.load(arquivo) # Carrega o arquivo .json para uma variável

remove('Arquivo_Json.json')