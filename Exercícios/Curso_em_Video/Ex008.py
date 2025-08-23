# Escreva um programa que leia um valor em metro e o exiba
# convetido em centímetros e milímetros.
m = float(input('Digite seu valor em metros '))
ce = float(m*100)
mi = float(m*1000)
print('O seu valor em centímetros é {} \nO seu valor em milímetros é {}'.format (ce, mi))