# Usamos o ANSI para definir estilo,  cor do texto, e cor do fundo dos caractéres
# Style 0 = Nenhum | 1 = Negrito | 4 = Sublinhado | 7 = Inventer cor do texto e cor do fundo
# Text 30 = Branco | 31 = Vermelho | 32 = Verde | 33 = Amarelo | 34 = Azul | 35 = Magenta | 36 = Ciano | 37 = Cinza
# Background 40 = Branco | 41 = Vermelho | 42 = Verde | 43 = Amarelo | 44 = Azul | 45 = Magenta | 46 = Ciano | 47 = Cinza
print('\033[7;47mTeste\033[m')

a, b = 5, 10

print(f'Os valores são \033[31m{a}\033[m e \033[32m{b}\033[m!')

print('\033[1;31mErro\033[m')
print('\033[1;32mCerto\033[m')