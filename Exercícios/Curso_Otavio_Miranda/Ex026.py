# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON e depois crie novamente as instâncias da classe com os dados salvos
# Faça em arquivos separados.
import json

CAMINHO_ARQUIVO = 'Pessoas.json'

class Pessoa:
    def __init__(self, nome, idade, hobby):
        self.nome = nome
        self.idade = idade
        self.hobby = hobby

def salvar(*objeto, caminho):
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        json.dump(objeto, arquivo, indent=2, ensure_ascii=False)

pessoa_1 = Pessoa('Eder', 15, 'Comer')
pessoa_2 = Pessoa('Giovana', 17, 'Dar')

pessoa1_dict = {'Nome': pessoa_1.nome, 'Idade': pessoa_1.idade, 'Hobby': pessoa_1.hobby}
pessoa2_dict = {'Nome': pessoa_2.nome, 'Idade': pessoa_2.idade, 'Hobby': pessoa_2.hobby}

salvar(pessoa1_dict, pessoa2_dict, caminho=CAMINHO_ARQUIVO)

with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

    for pessoa in dados:
        print(pessoa)