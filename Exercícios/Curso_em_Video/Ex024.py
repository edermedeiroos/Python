# Crie um programa que leia um nome de uma cidade, e diga se ela começa ou não
# com a palavra "Santo"
n = input('Digíte o nome da cidade: ')
ci = n.strip()
cid = ci.capitalize()
print('A cidade {} começa com a palavra "Santo"?\n{}'.format(cid, 'Santo' in cid.split()[0]))
