# ABSTRAÇÃO | Criação de uma classe genérica(classe abstrata) que contém métodos abstratos. São declarados na classe abstrata, mas não possuem uma implementação específica.
# As subclasses herdam a classe abstrata e são responsáveis por implementar os métodos abstratos de acordo com suas necessidades específicas.
# Envolve uma hierarquia de Classes. A classe abstrata fornece a base genérica e as subclasses aprimoram e implementam os detalhes específicos

from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt' # Arquivo.txt no mesmo caminho que __main__ com nome 'log'

class Log: # Classe abstrata
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log') # Erro levantado para usuario não utilizar está classe, apenas classes filhas

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')


class LogFileMixin(Log): # Subclasse
     def _log(self, msg):
        msg_fomatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando no log:', msg_fomatada)
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_fomatada)
            arquivo.write('\n')


class LogPrintMixin(Log): # Subclasse
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


if __name__ == '__main__': # Checa se o módulo executado é o atual(__main__) | Caso estja sendo importado não executa
    log = LogPrintMixin()
    log.log_error('qualquer coisa')
    log.log_success('Que legal')
    lprint_mixin = LogPrintMixin()
    lprint_mixin.log_error('qualquer coisa')
    lprint_mixin.log_success('Que legal')
    lfile_mixin = LogFileMixin()
    lfile_mixin.log_error('qualquer coisa')
    lfile_mixin.log_success('Que legal')

# Classes abstratas - Abstract Base Class (abc)
# ABC's são usadas como contratos para a definição de novas classes. Podem forçar outras classes a criarem métodos concretos.
# Também podem ter métodos concretos por elas mesmas. @abstractmethods são métodos que não têm corpo.
# Classes abstratas com métodos abstratos NÃO DEVEM ser instânciadas diretamente. Métodos abstratos DEVEM ser implementados nas subclasses (@abstractmethod)
# Uma classe abstrata em Python tem sua metaclasse(classe criadora de classes) sendo ABCMeta.

from abc import ABC, abstractmethod

class Log(ABC):
    @abstractmethod
    def _log(self, msg): ...

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})') # Implementou o corpo do método abstrato

# l = Log() | TypeError: Can't instantiate abstract class Log with abstract method _log
l = LogPrintMixin()
l.log_error('Oi')

# É possível criar @property | @setter | @classmethod | @staticmethod | @method como abstratos, para isso use @abstractmethod como decorator mais interno.
# Foo - Bar são palavras usadas como placeholder para palavras que podem mudar na programação.

class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    @abstractmethod
    def name(self, name): ...


class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        # print('Sou inútil')

    @AbstractFoo.name.setter
    def name(self, name):
        self._name = name


foo = Foo('Bar')
print(foo.name)