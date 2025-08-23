# Crie um programa que leia o nome e o preço de vários produtos
# O programa deve perguntar ao usúario se ele quer continuar.
# No final mostre:
# Qual o total gasto na compra | Quantos produtos custam mais de 1000 reais | O nome do produto mais barato
print('MERCADO')
print()
print('*'*50)
print()
cont = 1
cont1000 = 0
nome = input('Nome do produto {}: '.format(cont))
preco = float(input('Valor do produto {}: R$'.format(cont)))
continuar = input('Quer continuar ? ').strip().upper()
menor = preco
nomemenor = nome
soma = preco
if preco >= 1000:
    cont1000 += 1
if continuar in 'SIM':
    while True:
        cont += 1
        nome = input('Nome do produto {}: '.format(cont))
        preco = float(input('Valor do produto {}: R$'.format(cont)))
        continuar = input('Quer continuar? ').strip().upper()
        soma += preco
        if preco <= menor:
            nomemenor = nome
            menor = preco
        if preco >= 1000:
            cont1000 += 1
        if continuar not in 'SIM':
            break
print()
print('O total da compra foi R${} | Dentre os {} produtos, {} foram acima de R$1.000 | O produto mais barato foi {}(R${})'.format(soma, cont, cont1000, nomemenor, menor))
