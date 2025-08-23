# Crie um cógido python que teste se o site Pudim está acessível pelo computador usado
import urllib.request
try:
    site = urllib.request.urlopen('http://pudim.com.br')
except ConnectionError:
    print(' • Acesso ao site pudim.com.br | \033[031mNEGADO!\033[m')
else:
    print(' • Acesso ao site pudim.com.br | \033[032mPERMITIDO\033[m')
