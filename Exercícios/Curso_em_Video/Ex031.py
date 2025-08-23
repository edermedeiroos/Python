# Desenvolva um programa que leia a distância da viagem e calcule o preço da passagem
# Cobrando R$0.50 por km para viagens até 200km e R$0.45 para viagens mais longas
dis = float(input('Digíte a distância da viagem para saber o custo: '))
print()
print('|', '-'*50, '|')
print()
if dis<=200:
    print('O valor total da sua viagem de {}km é de R${}'.format(dis, dis*0.5))
else:
    print('O valor total da sua viagem de {}km e de R${}'.format(dis, dis*0.45))