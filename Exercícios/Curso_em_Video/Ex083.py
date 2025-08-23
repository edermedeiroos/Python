# Crie um programa onde o usúario digite uma expressão matemática qualquer que use parênteses
# Seu aplicativo deverá analisar se os parênteses estão abertos e fechados na ordem correta
print('VALIDAÇÃO DE EXPRESSÕES')
print()
print('*'*50)
print()
conta = input('Digite a expressão com parênteses desejada: ')
if conta.count('(') == conta.count(')') == 1:
    if conta.count('()') > 0:
        print('A expressão extá incorreta!')
    elif conta.find(')') < conta.find('('):
        print('A expressão está incorreta!')
    else:
        print('A expressão está correta!')
elif conta.count('(') == conta.count(')') == 0:
    print('A expressão não contém parênteses.')
else:
    print('A expressão está incorreta!')
