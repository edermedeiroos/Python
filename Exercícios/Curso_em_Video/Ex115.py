# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto
# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas
from Módulos import Sistema
arq = 'Cadastro.txt'
if not Sistema.arquivoexiste(arq):
    print('"Cadastro.txt" - \033[1;032mCRIADO\033[m')
    Sistema.criararquivo(arq)
Sistema.menuprint('Exibir cadastros', 'Cadastrar novo usúario', 'Encerrar sistema')
Sistema.menu()