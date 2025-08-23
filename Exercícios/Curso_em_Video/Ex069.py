# Crie um programa que leia a idade e o sexo de várias pessoa.
# A cada pessoa cadastrada, o programa deverá perguntar ao usúario se ele quer ou não continuar
# No final, o programa mostrará:
# Quantas pessoas tem mais de 18 anos | Quantos homens foram cadastrados | Quantas mulheres tem menos de 20 anos
print('CADASTRADOR')
print()
print('*'*50)
print()
cont = 1
idade = int(input('Idade da pessoa {}: '.format(cont)))
sexo = input('Sexo da pessoa {} [M/F]: '.format(cont)).strip().upper()
continuar = input('Quer cadastrar mais pessoas? ').strip().upper()
contmaior = 0
conthomem = 0
contmulher = 0
if idade >= 18:
    contmaior = 1
if sexo in 'M':
    conthomem = 1
if sexo in 'F' and idade < 20:
    contmulher = 1
print('-'*30)
if continuar in 'SIM':
    while True:
        cont += 1
        idade = int(input('Idade da pessoa {}: '.format(cont)))
        sexo = input('Sexo da pessoa {} [M/F]: '.format(cont)).strip().upper()
        continuar = input('Quer cadastrar mais pessoas? ').strip().upper()
        print('-' * 30)
        if idade >= 18:
            contmaior += 1
        if sexo in 'M':
            conthomem += 1
        if sexo in 'F' and idade < 20:
            contmulher += 1
        if continuar not in 'SIM':
            break
print()
print('Das {} cadastradas, {} são maiores de 18 anos, {} são homens, e {} são mulheres menores de 20 anos.'.format(cont, contmaior, conthomem, contmulher))
print()
print('----------------------------- PROGRAMA ENCERRADO -----------------------------')
