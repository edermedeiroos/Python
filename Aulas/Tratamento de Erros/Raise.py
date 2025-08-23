# RAISE
# Utilizado para disparar excessões no nosso código

def divide(num, div):
    nao_aceito_zero(div)
    return num/div

def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('É impossível dividir por 0')
    return True
