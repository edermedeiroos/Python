import os
lista = []
while True:
    escolha = input('- Selecione uma opção -\n• [i]nserir | [a]pagar | [l]istar: ').strip().lower()[0]
    if escolha in 'i':
        inserir = input('O que deseja inserir na lista? ')
        lista.append(inserir)
        os.system('cls')
    elif escolha in 'a':
        apagar = int(input('Digíte o índice que deseja apagar: '))
        if apagar in range(len(lista)):
            del lista[apagar]
            os.system('cls')
        else:
            print('Este índice não existe!')
        os.system('cls')
    elif escolha in 'l':
        if not lista:
            print('- Lista vazia!')
        else:
            for i, item in enumerate(lista):
                print(f'      • {i} - {item}')
