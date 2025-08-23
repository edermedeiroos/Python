# Utilizamos o try except para tratar erros que excedam ao executar o código
# Try para "tentarmos" executar o código
# Except para orientarmos o que fazer em caso de erro (exception) no nosso código
# Else para caso não ocorra erro nenhum
# Finally para executar um código independente de erro ou excessão

try: 
    a = int(input('Valor 1: '))
    b = int(input('Valor 2: '))
    r = a / b
except ZeroDivisionError:
    print('Não é possivel dividir o valor por 0')
except KeyboardInterrupt:
    print('O úsuario interrompeu a digitação')
except (ValueError, TypeError) as error:
    print('Erro com os tipos de dados digitados')
    print('Nome:', error.__class__.__name__)
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre :)')

# RAISE
# Utilizado para disparar excessões no nosso código

def divide(num, div):
    nao_aceito_zero(div)
    return num/div

def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('É impossível dividir por 0')
    return True
