primeiro = input('Digíte um valor: ')
segundo = input('Digíte outro valor: ')
if primeiro > segundo:
    print(f'{primeiro} é maior que {segundo}')
elif primeiro == segundo:
    print(f'{primeiro} é igual a {segundo}')
else:
    print(f'{primeiro} é menor que {segundo}')