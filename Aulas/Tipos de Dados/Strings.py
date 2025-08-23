# print('dentro de aspas é uma str (string)')
# Tipo de dado

print('STRING COMUM:')
print()
print('Olá, Mundo!')
print("""Texto longooooooooooooooooo
ooooooooooooooooooooooooooo
ooooooooooooooooooooooooooo
ooooooooooooooooooooooooooo""")
print('-'*20)

# FATIAMENTO
# Dentro de uma string temos os caractéres, cada caractér ocupa um espaço
# Primeiro caractér = 0 | Segundo caractér = 1, e assim por diante
# Podemos fatiar uma strin atravez das listas | ex:
frase = 'Eder tmj'
print('FATIAMENTO DA STRING:')
print()
print(frase[5]) # mostra caractére que ocupa a posição 5
print(frase[0:4],'ou',frase[:4]) # mostra os caractéres que ocupam da posição 0 ao 3
print(frase[0:5:2],'ou',frase[5::2]) # caractéres pulando de 2 em 2 caractéres
print(frase[5:]) # caractéres restantes a partir da letra 5
print(frase[:5]) # caractéres anteriores
print(frase[-1]) # caractéres exibidos de trás pra frente
print('-'*20)

# ANÁLISE
# funções para análise da string
print('ANÁLISE DA STRING')
print()
print(len(frase)) # conta o número de caractéres
print(frase.count('o'),'ou',frase.count('o',0,11)) # conta o número de caractéres específicos
print(frase.find('gos')) # mostra a partir de qual caractére começa determinada parte
print(frase.rfind('a')) # mostra a partir de qual caractére começa determinada parte pelo lado direito
print(frase.find('Dara')) # exibira -1 pois não contem 'Dara' na string
print('Eder' in frase) # exibira True ou False
print('-'*20)

# TRANSFORMAÇÃO
# funções para transformação em string
print('TRANSFORMAÇÃO DA STRING')
print()
print(frase.replace('Eder','gostosão')) # substituirá o primeiro termo pelo segundo
print(frase.upper()) # deixará a string inteira em maiúsculo
print(frase.lower()) # deixará a string inteira em minúsculo
print(frase.capitalize()) # deixara a string inteira em minúsculo menos o primeiro caractér
print(frase.title()) # transformara o primeiro caractér de cada palavra em maiúsculo
nova_frase = '            Eder muito gostosão demais nossa aff          '
print(nova_frase.strip()) # removera espaços iniciais e espaços finais
print(nova_frase.rstrip()) # remove apenas espaços direitos
print(nova_frase.lstrip()) # remove apenas espaços esquerdos
print('-'*20)

# DIVISÃO
# funções para divisão da string
print('DIVISÃO DA STRING')
print()
print(frase.split()) # Dividira as palavras espaçadas, criando novas strings | string -> lista
print('-'.join(frase)) # juntara cada elemento de acordo com o caractér aspeado
print('-'.join(frase.split())) # juntara cada palavra com o caractér aspeado

# FORMATAÇÃO
# adicionar variavéis dentro de strings através de formatações
n1 = 10
n2 = 5
soma = n1 + n2

print('A soma de {} + {} é {}'.format(n1, n2, soma)) # Atravéz do .format
print(f'A soma de {n1} + {n2} é {soma}') # Atravéz da fstring
print('A soma de %i + %i é %i' % (n1, n2, soma)) # Atravéz da interploação
