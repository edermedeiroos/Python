# As condições servem para possibilidades a depender de uma opção escolhida
# usamos if (se) e else (senão)
# podemos utilizar and (e), para adicionar mais de uma condição no if
# podemos utilizar or (ou), para dar possibilidades as condições
# podemos utilizar elif para adicionar condições dentro do if

# CONDIÇÕES SIMPLES | Aquelas que utilizam somente uma condição (if)
# CONDIÇÕES COMPOSTAS | Aquelas que utilizam mais de uma condição (if, elif, else)

print('CONDIÇÃO COMPOSTA')
print('-'*50)
tempo = int(input('Tempo de vida do Carro: '))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')

# CONDIÇÕES ANINHADAS | Condições dentro de outras condições
print('CONDIÇÕES ANINHADAS')
print('-'*50)
nome = str(input('Digite seu nome: '))
if nome == 'Eder':
    print('Teu nome é bonito pra porr tmj')
elif nome == 'Giovana':
    print('Krlh frajola tmj mó gostosa vc bjao')
elif nome in 'Paula, Rafa, Gabrielly, Gabriela, Alex, Santos, Bassaco':
    print('Nome de homosexxual')
else:
    print('Vsfd qm t chamou aqui')

# OPERAÇÕES TERNÁRIAS
# Condições escritas em apenas uma linha

condição = 10 == 10
mostra = 'Verdade' if condição else 'Mentira'
print(mostra)