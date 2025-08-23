# Relações entre classes: associação, agregação e composição
# ASSOCIAÇÃO | Tipo de relação onde os objetos estão ligados dentro do sistema | Essa é a relação mais comum entre objetos
# Geralmente, temos uma associação quando um objeto tem um atributo que referencia outro objeto.
# A associação não especifica como um objeto controla o ciclo de vida de outro objeto.

class Escritor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo'


escritor = Escritor('Luiz')
caneta = FerramentaDeEscrever('Caneta Bic')
maquina_de_escrever = FerramentaDeEscrever('Máquina')
escritor.ferramenta = maquina_de_escrever

print(caneta.escrever())
print(maquina_de_escrever.escrever())
print(escritor.ferramenta.escrever())

# AGREGAÇÃO | Forma mais especializada de associação entre dois ou mais objetos. Cada objeto terá seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode se tratar de uma relação onde um objeto precisa de outro para fazer determinada tarefa.

class Carrinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum([prod.preco for prod in self._produtos])

    def inserir_produtos(self, *produtos):
        for produto in produtos:
            self._produtos.append(produto)

    def listar_produtos(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()
p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20)
carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())

# COMPOSIÇÃO | Especialização da agregação.
# Nela, quando o objeto "pai" for apagado, todas as referências dos objetos filhos também são apagadas.

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero)) # Cria está instancia dentro da class Cliente | Local de composição

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self): # Dunder (__) que apga determinado valor
        print('Apagando', self.nome)

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('Apagando', self.rua, self.numero)

cliente1 = Cliente('Maria')
cliente1.inserir_endereco('Joel Braz', 466)
cliente1.inserir_endereco('Helio Cortez', 320)
cliente1.listar_enderecos()

del cliente1 # Deleta tanto o cliente quanto o endereço devido a relação de composição