def leiadinheiro(msg):
    print(msg, end='')
    p = input().strip().replace(' ', '')
    while True:
        if p.isnumeric():
            return int(p)
        elif p.replace('.', '').isnumeric():
            return float(p)
        elif p.replace(',', '').isnumeric():
            return float(p.replace(',', '.'))
        else:
            print(f'\n\033[031mERRO | "{p}" Não é um valor válido!\033[m\n')
            p = input(msg)