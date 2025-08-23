while True:
    print(f'{" CALCULADORA ":-^50}')
    print()
    try:
        n1 = float(input(' • Primeiro valor: '))
        n2 = float(input(' • Segundo valor: '))
    except:
        print('--- \033[031mERRO\033[m --- Dados inválidos!')
    print(f'\n{" OPERAÇÔES ":-^50}\n')
    print('     → 1 - Adição (+) | 2 - Subtração (-) | 3 - Multiplicação (x) | 4 - Divisão (/)')
    op = int(input('\n- Operação desejada: '))
    if op == 1:
        print(f'\n    {n1} + {n2} = {n1 + n2}\n')
    elif op == 2:
        print(f'\n    {n1} - {n2} = {n1 - n2}\n')
    elif op == 3:
        print(f'\n    {n1} x {n2} = {n1 * n2}\n')
    elif op == 4:
        print(f'\n    {n1} / {n2} = {n1 / n2}\n')
    else:
        print('--- \033[031mERRO\033[m --- Operação inválida!')
    sair = input('Encerrar? [S/N]: ').strip().upper()[0]
    if sair in 'S':
        break
