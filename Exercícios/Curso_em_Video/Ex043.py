# Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC, e mostre seu status:
# Abaixo de 18.5 = Abaixo do peso | Entre 18.5 e 25 = Peso ideal | 25 até 30 = Sobrepeso
# 30 até 40 = Obesidade | Acima de 40: Obesidade mórbida
print('CALCULADORA IMC')
print()
print('*'*50)
print()
p = float(input('Peso em quilos: '))
a = float(input('Altura em metro: '))
imc = p/(a**2)
print()
print('\033[1;34mCALCULANDO IMC\033[m')
print()
if imc < 18.5:
    print('Seu IMC é {:.1f} | Status: \033[1;35mABAIXO DO PESO\033[m'.format(imc))
elif 18.5 <= imc <= 25:
    print('Seu IMC é {:.1f} | Status: \033[1;32mPESO IDEAL\033[m'.format(imc))
elif 25 < imc <= 30:
    print('Seu IMC é {:.1f} | Status: \033[1;33mSOBREPESO\033[m'.format(imc))
elif 30 < imc <= 40:
    print('Seu IMC é {:.1f} | Status: \033[1;31mOBESIDADE\033[m'.format(imc))
else:
    print('Seu IMC é {:.1f} | Status: \033[1;35mOBESIDADE MÓRBIDA\033[m'.format(imc))
