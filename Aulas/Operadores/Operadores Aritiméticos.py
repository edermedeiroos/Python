# Adição: Representado pelo +
print('Conta_1 =', int(3 + 4))
# Subtração: Representado pelo -
print('Conta_2 =', int(4 - 3))
# Multiplicação: Representado pelo *
print('Conta_3 =', int(3 * 4))
# Divisão: Representado pela /
print('Conta_4 =', float(4/3))
# Potenciação: Representado pelos **
print('Conta_5 =', int(4**2))
# Divisão Inteira : Representado pelas // - significa a divisão somento por números inteiros
print('Conta_6 =', int(4//3))
# Resto da Divisão : Representado pela % - siginifca o resto de divisões resultantes em números inteiros
print('Conta_7 =', int(4 % 3))

# ORDEM DE PRECEDÊNCIA
# Primeiro Lugar = () -> Operações dentre de parênteses
# Segundo Lugar = ** -> Operações com exponenciação
# Terceiro Lugar = * / // % -> Operações com multiplicação, divisão, divisão inteira e resto da divisão
# Quarto Lugar = + - -> Operações com soma e subtração

# EXEMPLOS
print()
print(int(5+3*2))
print(int(3*5+4**2))
print(int(3*(5+4)**2))
print(int(81**(1/2)))

n1 =int(input('Digite um valor'))
n2 =int(input('Digite outro valo'))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
e = n1**n2
di = n1//n2
rd = n1%n2
print('A soma é {}, a subtração é {}, a mutliplicação é {}, '.format(s, sub, m), end='')
print('a divisão é {}, a exponenciação é {}, '. format(d, e), end='')
print('a divisão inteira é {} e o resto da divisão é {}.'.format(di, rd))