# Crie uma tupla, preenchida com os 20 primeiro colocados da tebela do brasileirão na ordem de colocação
# Depois mostre
# Apenas os primeiro 5 colocados | Os ultimos 4 colocados
# Uma lista com os times em ordem afabética | Em que colocação está o Palmeiras
print('BRASILEIRÃO')
print()
print('*'*50)
print()
tabela = ('BOTAFOGO', 'GRÊMIO', 'FLAMENGO', 'PALMEIRAS', 'ATHLETICO-PR', 'SÃO PAULO',
          'FLUMINENSE', 'RED BULL BRAGANTINO', 'FORTALEZA', 'INTERNACIONAL',
          'CRUZEIRO', 'CUIABÁ', 'ATLÉTICO-MG', 'SANTOS', 'CORINTHIANS',
          'GOIÁS', 'BAHIA', 'CORITIBA', 'AMÉRICA-MG', 'VASCO')
print(f'20 primeiros times do brasileirão: {tabela}')
print('-'*50)
print(f'Os primeiros 5 colocados do brasileirão são: {tabela[0:6]}.')
print('-'*50)
print(f'Os ultimos 4 colocados do brasileirão são: {tabela[-4:]}.')
print('-'*50)
print(f'A lista de times em ordem alfabética é {sorted(tabela)}')
print('-'*50)
print(f'O palmeiras está na {tabela.index("PALMEIRAS") + 1} posição.')
print()
print('------------------------------------ PROGRAMA ENCERRADO ------------------------------------')
