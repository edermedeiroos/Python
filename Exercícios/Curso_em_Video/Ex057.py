# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
print('LEITURA DE SEXO')
print()
print('*'*50)
print()
sexo = input('Digite seu sexo [M/F]: ').upper().strip()[0]
while sexo not in 'MmFf':
    sexo = input('Resposta inválida, digite novamente: ').upper().strip()[0]
print()
print('Sexo {} registrado com sucesso.'.format(sexo))
print('Obrigado pela resposta')