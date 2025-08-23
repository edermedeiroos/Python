perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
    {
        'Pergunta': 'Quanto é 57*5?',
        'Opções': ['570', '250', '285', '300'],
        'Resposta': '285',
    }
]

acertos = 0
for dic in perguntas:
    print(dic['Pergunta'], end='\n') # Mostra a pergunta

    print('OPÇÕES:\n') # Mostra as opções
    for indice, opcao in enumerate(dic['Opções']):
        print(f'{indice}) {opcao}')

    print()
    resposta = str(input('Escolha uma opção: ')).strip() # Pergunta a alternativa correta
    correta = str(dic['Opções'].index(dic['Resposta'])) # Localiza o indice da alternativa correta
    if resposta in correta: # Verifica se o usúario acertou
        print('\n👍 ACERTOU!!!')
        print('-'*50)
        acertos += 1
    else:
        print(f'\n❌ ERROU!!! A alternativa correta era {correta}')
        print('-'*50)

print(f'- PARABÉNS! \n   • Você acertou: {acertos} perguntas de {len(perguntas)}')