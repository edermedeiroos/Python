# BREAK
# Utilizamos o break para quebrar a repetição, adicionando uma condição a ele
# Utilizamos while True para uma repetição infinita

n = s = 0
while True:
    n = int(input('Digite um número'))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')