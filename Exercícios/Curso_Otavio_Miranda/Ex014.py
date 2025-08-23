def formatação(cpf):
    if cpf.count('.') > 0:  # Verifica se o usúario digitou pontos
        cpf = cpf.replace('.', '')
    if cpf.count('-') > 0:  # Verifica se o usúario digitou traços
        cpf = cpf.replace('-', '')
    return cpf


def somaNums(cpf, dígitos = 9, numRegressivo=10):
    soma = 0
    for n in cpf[:dígitos]:  # Define os 9 primeiros dígitos
        soma += int(n) * numRegressivo  # Faz a soma de cada um dos 9 primeiros dígitos 
        numRegressivo -= 1  # Contagem regressiva da multiplicação
    return soma


def validação(soma, Digito1):
    primeiro = (soma * 10) % 11
    if primeiro == 10:  # Verifica se o resto de divisão resultou em 10
        primeiro = 0
    if primeiro == int(Digito1):  # Verifica se o Digito 1 é igual ao primeiro da nossa função
        return True
    else:
        return False


def invalidos(cpf):
    invalidos = [
        11111111111,
        22222222222,
        33333333333,
        44444444444,
        55555555555,
        66666666666,
        77777777777,
        88888888888,
        99999999999
    ]
    if cpf in invalidos:
        return False
    else:
        return True


cpf = str(input('Digíte seu CPF: '))  # Pergunta o CPF
cpf_formatado = formatação(cpf)  # Formata o CPF
somaNove = somaNums(cpf_formatado)  # Faz a soma dos 9 primeiros dígitos do CPF
somaDez = somaNums(cpf_formatado, 10, numRegressivo=11)  # Faz a soma dos 10 primeiro dígitos do CPF
if validação(somaNove, cpf_formatado[9]) and invalidos(int(cpf_formatado)):
    # Valida o décimo dígito do CPF e confere se não está na lista de inválidos
    if validação(somaDez, cpf_formatado[10]) and invalidos(int(cpf_formatado)):
        # Valida o décimo primeiro dígito do CPF e confere se não está na lista de inválidos
        print(f'O CPF {cpf} é \033[1;032mVÁLIDO\033[m!!!')
    else:
        print(' - \033[1;031mERRO\033[m - CPF INVÁLIDO!!!')
else:
    print('- \033[1;031mERRO\033[m - CPF INVÁLIDO!!!')
