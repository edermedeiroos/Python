from random import randint

cpf = ''
for i in range(0, 11):
    cpf += str(randint(0, 9))

cpf_formatado = f'{cpf[0]}{cpf[1]}{cpf[2]}.{cpf[3]}{cpf[4]}{cpf[5]}.{cpf[6]}{cpf[7]}{cpf[8]}-{cpf[9]}{cpf[10]}'

print(f'O CPF aleatorizado foi: {cpf_formatado}')