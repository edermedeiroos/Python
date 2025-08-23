# Crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas ainda não
# atingiram a maioridade, e quantas já atingiram a maioridade
# Considere a maioridade 21 anos
import datetime
print('MAIORIDADE')
print()
print('*'*50)
print()
atual = datetime.date.today().year
num = 0
for c in range(1, 8):
    i = int(input('Ano de nascimento | Pessoa {}: '.format(c)))
    if i <= (atual - 21):
        num += 1
print()
print('Das 7 pessoas, apenas \033[1;033m{}\033[m são maiores de idade'.format(num))