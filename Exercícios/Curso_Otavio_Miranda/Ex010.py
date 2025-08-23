frase = """O Python é uma linguagem de programação\
 multiparadigma. Python foi criado por Guido van Rossum."""

i = 0
vezes_mais_aparece = 0
mais_aparece = ''
frase_formato = frase.strip().lower().replace(' ', '')
while i < len(frase_formato):
    letra_atual = frase_formato[i]
    contagem_letra_atual = frase_formato.count(letra_atual)
    if contagem_letra_atual > vezes_mais_aparece:
        vezes_mais_aparece = contagem_letra_atual
        mais_aparece = letra_atual
    i += 1
print(f'A letra que mais apareceu foi "{mais_aparece}" tendo sido {frase_formato.count(mais_aparece)} vezes')