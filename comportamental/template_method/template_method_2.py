"""
Template Method (comportamental) tem a intenção de definir
um algoritmo em um método, postergando alguns passos
para as subclasses por herança. Template method permite
que subclasses redefinam certos passos de um algoritmo
sem mudar a estrutura do mesmo.

Também é possível definir hooks para que as subclasses
utilizem caso necessário.

The Hollywood principle: "Don't Call Us, We'll Call You."
(IoC - Inversão de controle)
"""
from abc import ABC, abstractmethod


class Pizza(ABC):
    def prepare(self):
        # template method
        self.add_ingretients()  # Abstract
        self.cook()  # Abstract
        self.cut()  # Concreto
        self.serve()  # Concreto

    def cut(self):
        print(f'Cortando a pizza: {self.__class__.__name__}')

    def serve(self):
        print(f'Servindo a pizza: {self.__class__.__name__}')

    @abstractmethod
    def add_ingretients(self): pass

    @abstractmethod
    def cook(self): pass


class AModa(Pizza):
    def add_ingretients(self):
        print('AModa: presunto, queijo, goiabada')

    def cook(self):
        print('AModa: cozinhando por 45min no forno a lenha')


class Veg(Pizza):
    def add_ingretients(self):
        print('Veg: adicionando ingredientes - goiabada, gengible, soja')

    def cook(self):
        print('Veg: cozinhando por 30min no forno a lenha')


if __name__ == '__main__':
    a_moda = AModa()
    a_moda.prepare()
    print()

    veg = Veg()
    veg.prepare()
