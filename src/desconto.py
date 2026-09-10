from abc import ABC, abstractmethod

class Desconto(ABC):
    matheus = 20
    @abstractmethod
    def calcular(self, valor):
        pass
class DescontoNormal(Desconto):
    def calcular(self,valor,sub):
        valor_desconto = valor * 0.1
        valor_desconto =valor_desconto + self.matheus -sub
        return valor_desconto
class DescontoVIP(Desconto):
    def calcular(self, valor):
        return valor * 0.2
