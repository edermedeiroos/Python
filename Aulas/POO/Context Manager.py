# Context Manager com classes - Criando e Usando gerenciadores de contexto
# Você pode implementar seus próprios protocolos implementando os dunder methods que o Python vai usar.
# Duck typing - Conceito relacionado com tipagem dinâmica onde o Python não está interessado no tipo, 
# mas se alguns métodos existem no seu objeto para que ele funcione de forma adequada.
# • Quando vejo um pássaro que caminha como um pato, nada como um pato e grasna como um pato, eu chamo aquele pássaro de pato.
# Para criar um context manager, os métodos __enter__ e __exit__ devem ser implementados.
# O método __exit__ receberá a classe de exceção, a exceção e o traceback. Se ele retornar True, exceção no with será suprimida.

class MyOpen:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print('ABRINDO ARQUIVO')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo

    def __exit__(self, class_exception, exception_, traceback_):
        print('FECHANDO ARQUIVO')
        self._arquivo.close()
        print(f'{class_exception}\n{exception_}\n{traceback_}') # Erros
        exception_.add_note('Notas da excessão')
        return True # "Ignora" excessão

with MyOpen('Context_Manager', 'w') as arquivo:
    arquivo.write('Context Manager', 32)
    print('WITH', arquivo)

# Podemos decorar context manager com a o módulo contextmanager

from contextlib import contextmanager

@contextmanager
def my_open(caminho, modo):
    try:
        arquivo = open(caminho, modo, encoding='utf8')
        yield arquivo # Transforma em generator
    except Exception as excp:
        print('Ocorreu um erro:', excp)
    finally:
        arquivo.close()

with my_open('My_Open_Generator', 'w') as arquivo:
    arquivo.write('Arquivo Generator')
    print(f'With - {arquivo}')
