"""
class Desconto:
    def calcular(self,tipo,valor)
        if tipo == "normal":
            return valor *0.1
        elif tipo == "vip":
            return valor *0.2
        elif tipo == "premium":
            return valor *0.3
"""

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
teste = DescontoNormal()
print(teste.calcular(100,2))

"""class greet(ABC):
    @abstractmethod
    def say_hello(self, nome):
        return "Hello " + nome
class greet2(greet):
    def say_hello(self, nome):
        return super().say_hello(nome) + " How are you? \n"
class greet3(greet2):
    def say_hello(self, nome, quantidade):
        return super().say_hello(nome) + " How are you? \n I am fine, thank you!" + str(quantidade)
teste = greet3()
print(teste.say_hello("Matheus", 5))"""