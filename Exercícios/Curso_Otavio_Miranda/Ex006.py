# Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
# descrito, exiba a saudação apropriada. Ex. 
# Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
hora = int(input('Que horas são? (Digíte apenas o valor inteiro): '))
if hora in (0, 11) or hora == 24:
    print('Bom dia!!!')
elif hora in (12, 17):
    print('Boa tarde!!!')
elif hora in (18, 23):
    print('Boa noite!!!')
else:
    print('Que horas são essas ? KKKKKKKK')