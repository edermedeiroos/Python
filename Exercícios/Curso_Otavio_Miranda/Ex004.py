# Peça ao usúario para digitar o nome, a idade, e exiba:
# O nome do usúario | O nome invertido | Se o nome contém espaços | O número de letras | A primeira e última letra
# Se nada for digitado exiba: desculpe, você deixou campos vazios
nome = input('Nome: ').strip()
idade = input('Idade: ')
if nome and idade: 
    print(f' • Seu nome é {nome}')
    print(f' • Seu nome invertido é {nome[::-1]}') 
    if nome.count(' ') > 0:
        cont = nome.count(' ')
        print(f' • Seu nome contém {cont} espaço(s)')
    else:
        print(' • Seu nome não contém espaços')
    print(f' • Seu nome contém {len(nome) - cont} letras')
    print(f' • A primeira letra do seu nome é "{nome[0]}" e a última "{nome[-1]}"')
else:
    print('Desculpe, você deixou campos vazios')
