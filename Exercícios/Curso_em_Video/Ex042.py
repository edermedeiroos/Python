# Refaço o desafio 35, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero = Todos os lados iguais | Isóceles = 2 lados iguais | Escaleno: Nenhum lado igual
print('TRIÂNGULOS')
print()
print('*'*50)
print()
r1 = float(input('Valor da reta 1: '))
r2 = float(input('Valor da reta 2: '))
r3 = float(input('Valor da reta 3: '))
if r1 == r2 == r3:
    print('Estas retas formam um triângulo \033[1;033mequilatero\033[m')
elif (r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1) and (r1 == r2 or r1 == r3 or r2 == r3):
    print('Estas retas formam um triângulo \033[1;033misóceles\033[m')
elif (r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1) and (r1 != r2 != r3):
    print('Estas retas formam um triângulo \033[1;033mescaleno\033[m')
else:
    print('Estas retas \033[1;031mnão\033[m podem formar um triângulo')
