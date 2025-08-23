# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas e no final mostre   :
# A média de idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres tem menos de 20 anos
print('COMPARADOR COMPLETO')
print()
print('*'*50)
print()
somaidade = 0
mediaidade = 0
maioridadeH = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('----- PESSOA {} -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadeH = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadeH:
        maioridadeH = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é {}'.format(mediaidade))
print('O homem mais velho tem {} e se chama {}'.format(maioridadeH, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
