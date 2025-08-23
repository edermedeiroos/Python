# POLIMORFISMO | Permite que classes deridavas de uma mesma superclasse tenham métodos iguais (com mesma assinatura) mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade de parâmetros (retorno não faz parte da assinatura)
# SOLID - Principios da programação orientada a objetos
# L - Princípio da substituição de liskov - Objetos de uma superclasse devem ser substituíveis por objetos de uma subclasse sem quebrar a aplicação.

from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, msg) -> None:
        self.mensagem = msg

    @abstractmethod
    def enviar(self) -> bool: ... # -> Define que este método deva retornar valor Booleano aos outros desenvolvedores

class NotificacaoEmail(Notificacao):
    def enviar(self):
        print(f'Email - Enviando: {self.mensagem}')
        return True # Segue o princípio de Liskov retornando valor Booleano definido na assinatura do método

class NotificacaoSMS(Notificacao):
    def enviar(self):
        print(f'SMS - Enviando: {self.mensagem}')
        return True # Segue o princípio de Liskov retornando valor Booleano definido na assinatura do método

def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação Enviada!')
    else:
        print('Notificação não enviada!') # Acontece caso o retorno não siga o princípio de Liskov | Não retorne valor definido na assinatura

notificar(NotificacaoEmail('Teste'))
notificar(NotificacaoSMS('Teste 2'))
