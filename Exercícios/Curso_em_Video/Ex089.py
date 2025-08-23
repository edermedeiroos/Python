# Crie um programa que leia nome, e duas notas de vários alunos e guarde tudo em uma lista composta
# No final, mostre um boletim contendo a média de cada um e permita que o usúario possa mostrar
# as notas de cada aluno individualmente.
print('MÉDIA ESCOLAR | LISTA')
print()
print('*'*50)
print()
lista = [[], [], []]
while True:
    nome = str(input('Nome do aluno: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista[0].append(nome)
    lista[1].append(media)
    lista[2].append(nota1)
    lista[2].append(nota2)
    continuar = input('Quer continuar? ').strip().upper()
    print()
    if continuar not in 'SIM':
        break
print('-='*25)
cont = 0
print(f"{'No.':<5}{'NOME':<15}{'MÉDIA':<5}")
print('-'*25)
for aluno in lista[0]:
    print(f'{cont:<5}{aluno:<15}{lista[1][cont]:>5}')
    cont += 1
print('-'*25)
while True:
    n = int(input('Mostrar as notas de qual aluno? [999] interrompe: '))
    if n == 999:
        break
    print(f'Notas de {lista[0][n]} são: {lista[2][(n * 2):(n * 2 + 2)]}')
    print('-'*50)
