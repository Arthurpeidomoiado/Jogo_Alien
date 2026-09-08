""

from abc import ABC, abstractmethod

class Desconto(ABC):
    matheus = 20
    @abstractmethod
    def calcular(self, valor):
        pass
class DescontoNormal(Desconto):
    def calcular(self,valor,sub):
        valor_desconto = valor * 0.1
        valor_desconto =valor_desconto + super().matheus -sub
        return valor_desconto
class DescontoVIP(Desconto):
    def calcular(self,valor,sub):
        valor_desconto = valor * 0.2
        valor_desconto =valor_desconto + super().matheus -sub
        return valor_desconto
class DescontoPremium(Desconto):
    def calcular(self,valor,sub):
        valor_desconto = valor * 0.3
        valor_desconto =valor_desconto + super().matheus -sub
        return valor_desconto
class Desconto_na_ativa(Desconto):
    def aplicar_Desconto(desconto: Desconto, valor, sub):
        return desconto.calcular(valor,sub)

teste = DescontoNormal()
print(teste.calcular(100,2))
print(Desconto_na_ativa.aplicar_Desconto(DescontoVIP(),100,2))
