# O encapsulamento é estabelecido a partir dos modificadores de acesso: public, protected, private | Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
# •   (sem underline) = public | Pode ser usado em qualquer lugar
# • _ (um underline) = protected | Não DEVE ser usado fora da classe ou suas subclasses.
# • __ (dois underlines) = private | "name mangling" em Python | Só DEVE ser usado na classe em que foi declarado | Para acesso exterior é necessário _NomeClasse__attrOuMethod

class Encapsulamento:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido'
        self.__exemplo = 'isso é private'

    def metodo_publico(self):
        print('metodo_publico')

    def _metodo_protected(self):
        print('_metodo_protected')

    def __metodo_private(self):
        print('__metodo_private')

