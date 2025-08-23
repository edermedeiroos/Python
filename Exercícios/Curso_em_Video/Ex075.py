# Desenvolva um programa que leia 4 valores pelo teclado, guarde-os em uma tupla,  e no final mostre:
# Quantas vezes apareceu o valor 9 | em que posição foi digitado o primeiro valor 3 | Quais foram os números pares
print('ANÁLISE | TUPLA')
print()
print('*'*50)
print()
nums = (int(input('Digíte um valor: ')),
        int(input('Digíte um valor: ')),
        int(input('Digíte um valor: ')),
        int(input('Digíte um valor: ')))
print()
print(f'O valor 9 foi digitado {nums.count(9)} vezes')
if nums.count(3) != 0:
    print(f'O valor 3 aparece a primeira vez na posição {nums.index(3) + 1}')
print('Os valores digitados pares foram: ', end='')
for n in nums:
    if n % 2 == 0:
        print(n, end=' | ')
print()
print('----------------------------- PROGRAMA ENCERRADO -----------------------------')
