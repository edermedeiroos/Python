# Python Special Methods | Magic Methods | Dunder Methods - Dunder = Double Underscore = __dunder__
# Todo objeto passa por um dunder method para executar sua determinada função
# Artigos: https://rszalski.github.io/magicmethods/ | https://docs.python.org/3/reference/datamodel.html#specialnames

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self): # Representação o objeto
        class_name = self.__class__.__name__
        return f'{class_name}: x = {self.x}, y = {self.y}'

    def __str__(self): # Representação do objeto obrigatóriamente como string
        return f'(x = {self.x} | y = {self.y})'

    def __add__(self, other): # Faz a soma de um objeto com outro
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)

    def __gt__(self, other): # Verifica se um objeto é maior que outro
        if self.x * self.y > other.x * other.y:
            return True
        return False

ponto_1 = Ponto(10, 20)
ponto_2 = Ponto(52, 39)
ponto_3 = ponto_1 + ponto_2

print(str(ponto_1))
print(repr(ponto_1))
print(f'{ponto_1!r}')
print(ponto_3)
print(ponto_1 > ponto_2)

# __new__ | Método responsável por criar e retornar o novo objeto. Por isso, new recebe cls. DEVE retornar o novo objeto
# __init__ é o método responsável por inicializar a instância. Por isso, init recebe self. NÃO DEVE retornar nada (None)

class A:
    def __new__(cls):
        instancia = super().__new__(cls)
        instancia.x = 123 # Variavel declarada a todas as instancias desta classe
        return instancia

    def __init__(self):
        print('Inicializando objeto')

    def soma(self):
        print(100 + self.x)

A()
A().soma()

# __call__ | Método responsável por executar a instância - Callable é algo que pode ser executado com parênteses

class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, *args, **kwargs):
        print(f'{kwargs.get(*kwargs)} está chamando: {self.phone}')

call = CallMe(999122612)
call(kwargs='Eder')