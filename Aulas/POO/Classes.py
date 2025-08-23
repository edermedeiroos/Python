# As classes geram novos objetos (instâncias) que podem ter seus próprios atributos (Valores assumidos pela classe) e métodos ("Funções").
# Os objetos gerados pela classe podem usar seus dados internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de classes.
# O método __init__ é o inicializador de atributos 
# O primeiro argumento do __init__ sempre recebe a característica self, independente do nome
# __dict__ ou a função vars() exibem os valores presentes em determinada instância

class Camera:
    atributo = 'Isso é um atributo ja que é assumido somente dentro da classe'

    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} JA está filmando')
            return

        self.filmando = True
        return print(f'{self.nome} começou a filmar')

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} não esta filmando')
            return

        self.filmando = False
        return print(f'{self.nome} parou de filmar')

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não consegue tirar fotos enquanto filma')
            return

        return print(f'{self.nome} está tirando foto!')

camera1 = Camera('Canon')
camera2 = Camera('Sony')

print(Camera.atributo)

print(camera1.nome)
camera1.filmar()
camera1.filmar()
camera1.fotografar()
camera1.parar_filmar()
camera1.fotografar()
camera1.filmar()

print(camera2.nome)
camera2.fotografar()
camera2.parar_filmar()

print(camera1.__dict__)
print(vars(camera1))

# @CLASSMETHOD
# Decora a classe e permite criar novos métodos fábrica (factoreis method) utilizando o cls(referente a classe) ao invéz do self(referente a instância)

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)


p1 = Pessoa('João', 34)
p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa('Anônima', 23)
p4 = Pessoa.criar_sem_nome(25)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)

# @STATICMETHOD
# Funções dentro do escpo da classe, porém sem acesso ao self e cls

class Classe:
    @staticmethod
    def funcao_que_esta_na_classe(*args, **kwargs):
        print('oi nao posso fazer nada sou inutil', args, kwargs)

# @PROEPRTY 
# Getter no modo Pythônico - um método para obter um atributo
# @property é uma propriedade do objeto - Um método que se comporta como um atributo
# Geralmente é usada para - Getter | Evitar quebra de código cliente(código que usa seu código) | Habilitar um setter | Executar ações recebendo um atributo
# getter → Obtém valor | setter → Define novo valor
# Por convenção, um atributo que começa com _ (ex: _cor), não devem ser usados fora da classe

class Caneta:
    def __init__(self, cor):
        self._cor_tinta = cor

    @property
    def cor(self):
        return self._cor_tinta
    
    @cor.setter
    def cor(self, valor):
        self._cor_tinta = valor

caneta = Caneta('Azul')
print(caneta.cor)
caneta.cor = 'Rosa'
print(caneta.cor)

# Para levantarmos erros e criar exceções em classes herdamos a classe Exception

class MeuErro(Exception):
    ...

class OutroErro(Exception):
    ...

def levantar():
    raise MeuErro('A mensagem do meu erro')

# É possível lançar outras excessões sobre uma excessão | The above exception was the direct cause of the following exception:
try:
    levantar()
except MeuErro as error:
    print(error.__class__.__name__)
    print(error.args)
    error.add_note('\n• Isso é uma nota na excessão | Podemos comunicar outros desenvolvedores')
    raise OutroErro('Lançando outro erro!') from error