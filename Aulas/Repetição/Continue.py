# CONTINUE
# Utilizamos o continue para pularmos a ação em determinada repetição

n = 0
while n <= 10:
    n += 1
    if n == 5:
        print('Não mostra o 5')
        continue
    print(n)