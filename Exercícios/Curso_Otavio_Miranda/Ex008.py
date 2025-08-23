nome = 'Eder Medeiros'
cont = 0
novo_nome = ''
while cont < len(nome):
    novo_nome += f'.{nome[cont]}'
    cont += 1
novo_nome += '.'
print(novo_nome)
