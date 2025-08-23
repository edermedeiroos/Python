# HERANÇA | Cria uma classe a partir de outra classe | Um nivel muito acima da associação agregação e composição
# Associação - Um Obj. usa outro Obj. | Agregação - Um Obj. tem outro Obj. | Composição - Obj. é dono de outro Obj. | Herança - Um Obj. é um outro Obj.
# Classe principal (Pessoa) -> super class, base class, parent class
# Classes filhas (Cliente) -> sub class, child class, derived class
# A herança segue o method resolution order (MRO), ou seja, ele executara primeiro os métodos ou atributos presentes na classe antes da herança | Vemos isso no help()

class Pessoa:
    cpf = '1234'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa):
    def falar_nome_classe(self):
        print('Seguindo o MRO')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Aluno(Pessoa):
    cpf = 'cpf do MRO'
    ...


c1 = Cliente('Luiz', 'Otávio')
c1.falar_nome_classe()
a1 = Aluno('Maria', 'Helena')
a1.falar_nome_classe()
print(a1.cpf)

# CLASSE super() E A SOBREPOSIÇÂO DE MÉTODOS
# Utilizamos a classe super() para se refererir a um método da classe herdada

class MinhaString(str):
     def upper(self):
         print('CHAMOU UPPER')
         retorno = super(MinhaString, self).upper()
         print('DEPOIS DO UPPER')
         return retorno


string = MinhaString('Luiz')
print(string.upper())

# HERANÇA MÚLTIPLA
# Herança simples: Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Herança múltipla e mixins: Log -> FileLog
# Cliente(Pessoa, FileLog) | Cliente herda Pessoa e classes herdadoras, junto de FileLog e classe herdadoras
# Para saber a ordem de chamada dos métodos use o método de classe Classe.mro() ou __mro__

class A:
    def quem_sou(self):
        print('A')


class B(A):
    def quem_sou(self):
        print('B')


class C(A):
    def quem_sou(self):
        print('C')


class D(B, C):
    def quem_sou(self):
        print('D')


d = D()
d.quem_sou()
print(D.mro())