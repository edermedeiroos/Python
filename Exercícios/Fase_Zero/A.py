C, G = map(int, input('Valores G e C: ').split())
if C == 1:
    print('Vivo e morto')
elif C == 0 and G == 1:
    print('Vivo')
else:
    print('Morto')