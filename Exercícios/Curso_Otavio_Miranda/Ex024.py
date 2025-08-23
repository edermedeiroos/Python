# Exercício - Lista de tarefas com desfazer e refazer

import os

lista_tarefas = []
desfeitos = []

print(f'\033[032m{"LISTA DE TAREFAS":^100}\033[m')

while True:
    print()
    resposta = input('Qual comando deseja executar? [Listar | Adicionar | Desfazer | Refazer]: ').strip().lower()
    if resposta in 'listar':
        if lista_tarefas:
            print()
            for tarefa in lista_tarefas:
                print(f'• {tarefa}')
        else:
            print('\n   • \033[031mLISTA VAZIA\033[m')
    elif resposta in 'adicionar':
        print()
        tarefa = str(input('    → Tarefa: '))
        lista_tarefas.append(tarefa)
    elif resposta in 'desfazer':
        try:
            desfeitos.insert(0, lista_tarefas.pop(-1))
        except:
            print('\n   • \033[031mNenhuma tarefa para desfazer!!!\033[m')
            continue
    elif resposta in 'refazer':
        try:
            refeito = lista_tarefas.append(desfeitos[0])
        except:
            print('\n   • \033[031mNenhuma tarefa para refazer!!!\033[m')
            continue
        desfeitos.pop(0)
    elif resposta in 'limpar':
        os.system('cls')
    else:
        print('\n   • \033[031mCOMANDO INVÁLIDO!!!\033[m')