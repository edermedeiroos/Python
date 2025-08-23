# Faça um programa que leia a largura e a altura de uma
# parede em metro, calcule a sua área e a quantidade de
# tinta necessário para pintá-la, sabendo que cada litro
# de tinta pinta uma área de 2m quadrados
largura = float(input('Largura da parede em metros: '))
altura = float(input('Altura da parede em metros: '))
a = largura * altura
t = a/2
print('Sua parede tem {:1f} metros quadrados\nSerá necessário {:1f} litros de tinta para pintá-la'.format (a, t))