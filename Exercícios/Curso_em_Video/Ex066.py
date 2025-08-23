# Refaça o exercício 64, mas agora com o comando break
print('LEITOR NÚMERO E SOMATÓRIA | BREAK')
print()
print('*'*50)
print()
cont = 1
nPrimeiro = int(input('Digite um valor a ser somado | [999] para sair: '))
nDiverso = int(input('Digite um valor a ser somado | [999] para sair: '))
soma = nPrimeiro
while True:
    if nDiverso == 999:
        break
    else:
        soma += nDiverso
        nDiverso = int(input('Digite um valor a ser somado | [999] para sair: '))
        cont += 1
print()
print('A soma dos {} termos é {}'.format(cont, soma))
print()
print('------------------------- PROGRAMA ENCERRADO -------------------------')