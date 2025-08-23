# Closure e funções que retornam outras funções

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

print(criar_saudacao())

print(criar_saudacao('Bom Dia')('Eder'))
print(falar_boa_noite('Eder'))
for nome in ['Dara', 'Marilda', 'Marcelino']:
    print(falar_bom_dia(nome))


# Closure podem decorar argumentos passados e executa-los depois:

def executa(funcao, arg):
    def interna(outro_arg):
        return funcao(arg, outro_arg)
    return interna

def soma(a, b):
    return a + b

soma_com_dez = executa(soma, 10)

print(soma_com_dez(34))