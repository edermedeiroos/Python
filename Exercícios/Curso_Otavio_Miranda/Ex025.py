# Exercício - Lista de tarefas com desfazer e refazer | Banco de dados .json

import json
import os


def listar(tarefas):
    print()
    if not tarefas:
        print(' → \033[031mNenhuma tarefa para listar\033[m\n')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t• {tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print(' → \033[031mNenhuma tarefa para desfazer\033[m\n')
        return

    tarefa = tarefas.pop()
    print(f'    - {tarefa=} \033[031mremovida\033[m da lista de tarefas.\n')
    tarefas_refazer.append(tarefa)


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print(' → \033[031mNenhuma tarefa para refazer\033[m\n')
        return

    tarefa = tarefas_refazer.pop()
    print(f'    - {tarefa=} \033[032madicionada\033[m na lista de tarefas.\n')
    tarefas.append(tarefa)

def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('- Você não digitou uma tarefa.')
        return
    print(f'    - {tarefa=} \033[032madicionada\033[m na lista de tarefas.\n')
    tarefas.append(tarefa)


def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('- \033[031mArquivo não existe\033[m')
        salvar(tarefas, caminho_arquivo)
    return dados


def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados


CAMINHO_ARQUIVO = 'Lista_de_Tarefas.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []

print(f'\033[032m{"LISTA DE TAREFAS":^100}\033[m')
while True:
    print(f'• Comandos: \033[033mLISTAR\033[m | \033[031mDESFAZER\033[m | \033[032mREFAZER\033[m')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('clear'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
        comandos['adicionar']
    comando()
    salvar(tarefas, CAMINHO_ARQUIVO)
