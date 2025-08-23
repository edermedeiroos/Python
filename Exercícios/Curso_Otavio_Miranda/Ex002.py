nome = str(input('Nome: '))
altura = float(input('Altura em metros: '))
peso = float(input('Peso em kilos: '))
imc = peso / altura ** 2
print(f' • Seu nome é {nome} | Você tem {altura}m | Pesa {peso} kg')
print(f' • O seu IMC é: {imc}')