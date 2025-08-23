# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário
# No final, mostre o conteúdo da estrutura na tela
print('MÉDIA | DICIONÁRIOS')
print()
print('*'*50)
print()
cadastro = dict()
cadastro['nome'] = str(input('Nome do aluno: '))
cadastro['media'] = float(input('Média do aluno: '))
if cadastro['media'] >= 7:
    cadastro['situação'] = 'Aprovado'
else:
    cadastro['situação'] = 'Reprovado'
print()
for k, v in cadastro.items():
    print(f'O campo {k} recebe: {v}')
