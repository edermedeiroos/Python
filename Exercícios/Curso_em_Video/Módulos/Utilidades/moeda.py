def dobro(preco=0, formato=True):
    preco *= 2
    if formato:
        return moeda(preco)
    else:
        return preco


def metade(preco=0, formato=True):
    preco /= 2
    if formato:
        return moeda(preco)
    else:
        return preco


def aumentar(preco=0, porcent=0, formato=True):
    preco += (porcent/100 * preco)
    if formato:
        return moeda(preco)
    else:
        return preco


def diminuir(preco=0, porcent=0, formato=True):
    preco -= (porcent/100 * preco)
    if formato:
        return moeda(preco)
    else:
        return preco


def moeda(preco=0, formato='R$'):
    return f'{formato}{preco:.2f}'.replace('.', ',')


def resumo(preco=0, mais=0, menos=0):
    """GIOVANA GOSTOSA"""
    print(f'{"MOEDA":^50}')
    print('-'*50)
    print(f'• O dobro de {moeda(preco)} é {dobro(preco)}')
    print(f'• A metade de {moeda(preco)} é {metade(preco)}')
    if mais > 0:
        print(f'• {moeda(preco)} com um aumento de {mais}% é {aumentar(preco, mais)}')
    if menos > 0:
        print(f'• {moeda(preco)} com uma diminuição de {menos}% é {diminuir(preco, menos)}')
    print('-'*50)