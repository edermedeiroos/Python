# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def motor(self, nome):
        self.nome_motor = Motor(nome).nome

    def fabricador(self, nome):
        self.nome_fabricador = Fabricante(nome).nome

    def informacoes(self):
        print(f'• Nome: {self.nome}')
        print(f'• Motor: {self.nome_motor}')
        print(f'• Fabricante: {self.nome_fabricador}')

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome='Desconhecido'):
        self.nome = nome

carro1 = Carro('Ferrari')
carro1.motor('Motor Bom')
carro1.fabricador('Ferrari')
carro1.informacoes()

carro2 = Carro('Fusca')
carro2.motor('Motor melhor ainda')
carro2.fabricador('Deus')
carro2.informacoes()