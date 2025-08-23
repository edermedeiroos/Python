# Crie um programa que tenha um função chamada voto() que vai receber como parâmetro o ano de nascimento desta pessoa
# retornando o valor literal indicando se essa pessoa tem voto negado, opcional ou obrigátorio nas eleições
def voto(ano):
    from datetime import datetime
    idade = datetime.today().year - ano
    if idade < 16:
        return f'   • Com {idade} anos o voto é: NEGADO!'
    elif 15 < idade < 18:
        return f'   • Com {idade} anos o voto é: OPCIONAL.'
    else:
        return f'   • Com {idade} anos o voto é: OBRIGATÓRIO!'


print('ACESSO AO VOTO | FUNÇÃO')
print()
print('-'*50)
print()
print(voto(int(input('Digite seu ano de nascimento: '))))
