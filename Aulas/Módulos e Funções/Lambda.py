# Lambda são funções anonimas (sem nome) de uma linha única

def executa(funcao, *args): # para executarmos determinada função
    return funcao(*args)

print(
    executa(
        lambda x, y: x + y, 
        2, 3 # 2 e 3 vão substituir os parâmetros x e y
    ),
)
soma = lambda x, y: x + y

print(soma(10, 20))

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

alunos.sort(key= lambda a: a['nome']) # Ordenara de acordo com a função anonima que indica a chave['nome']
print(*alunos, sep='\n')
lista_teste = {
    'nome': 'Eder',
    'idade': 18,
    'outro': 'teste'
    }
print(*lista_teste)