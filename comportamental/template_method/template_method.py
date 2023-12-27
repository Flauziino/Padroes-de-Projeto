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


class Abstract(ABC):
    def template_method(self):
        self.hook()
        self.operation1()
        self.base_class_method()
        self.operation2()

    @abstractmethod
    def operation1(self):
        pass

    @abstractmethod
    def operation2(self):
        pass

    def base_class_method(self):
        print('OLHA EU AE (abstract class)')

    def hook(self):
        pass


class ConcreteClass(Abstract):
    def hook(self):
        print('Vou utilizar o hook')

    def operation1(self):
        print('OPERACAO 1 CONCLUIDA')

    def operation2(self):
        print('OPERACAO 2 CONCLUIDA')


class ConcreteClass2(Abstract):
    def operation1(self):
        print('OPERACAO 1 CONCLUIDA (diferente)')

    def operation2(self):
        print('OPERACAO 2 CONCLUIDA (diferente)')


if __name__ == '__main__':
    c1 = ConcreteClass()
    c1.template_method()
    print()
    c2 = ConcreteClass2()
    c2.template_method()
