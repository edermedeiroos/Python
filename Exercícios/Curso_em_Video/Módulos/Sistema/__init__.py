def linha(tam=152):
    print('-'*tam)


def opcoes(*opcs):
    c = 1
    for opc in opcs:
        print(f'     • \033[33m{c}\033[m - \033[34m{opc}\033[m')
        c += 1


def menuprint(*opcs):
    print(f'\033[7;40m{"SISTEMA":^152}\033[m')
    linha()
    opcoes(*opcs)
    linha()


def menu():
    from time import sleep
    while True:
        try:
            escolha = int(input('\033[032mAcesso: \033[m'))
        except ValueError:
            print('→ \033[31mERRO\033[m | Favor digite um número inteiro válido!')
        except KeyboardInterrupt:
            print('\n→ \033[31mERRO\033[m | Usúario decidiu interromper a ação')
            break
        else:
            opcs = list(['', '', ''])
            if escolha < 1:
                print('→ \033[31mERRO\033[m | Favor digite uma opção válida!\n')
                sleep(0.5)
                menuprint('Exibir cadastros', 'Cadastrar novo usúario', 'Encerrar sistema')
            try:
                print(opcs[escolha - 1], end='')
                if escolha == 1:
                    print('     • \033[1;37mCADASTRADOS:\033[m')
                    with open('Cadastro.txt', 'r') as txt:
                        print(txt.read())
                        print()
                elif escolha == 2:
                    print('.'*50)
                    print(f'{"NOVO USÚARIO":^50}')
                    nome = input(' • Nome: ')
                    while True:
                        try:
                            idade = int(input(' • Idade: '))
                        except ValueError:
                            print('→ \033[31mERRO\033[m | Favor digite um número inteiro válido!')
                        else:
                            break
                    print('.'*50)
                    with open('Cadastro.txt', 'a', encoding='utf-8') as txt:
                        txt.write(f'\n\033[4m{nome}\033[m | \033[34m{str(idade)}\033[m')
                elif escolha == 3:
                    print(f'\n\033[31;7m{"-="*76}\n{"ENCERRANDO SISTEMA":^152}\n{"-="*76}\033[m')
                    break
            except IndexError:
                print('→ \033[31mERRO\033[m | Favor digite uma opção válida!\n')
                sleep(0.5)
                menuprint('Exibir cadastros', 'Cadastrar novo usúario', 'Encerrar sistema')
            except ValueError:
                print('→ \033[31mERRO\033[m | Favor digite um número inteiro válido!')
            except KeyboardInterrupt:
                print('\n→ \033[31mERRO\033[m | Usúario decidiu interromper a ação')
                break


def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('→ \033[31mERRO\033[m | Falha na criação do arquivo')