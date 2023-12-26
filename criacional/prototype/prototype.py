"""
Especificar os tipos de objetos a serem criados
usando uma instância-protótipo e criar novos objetos
pela cópia desse protótipo

Mutáveis (passados por referência)
  list
  set
  dict
  class (o usuário pode mudar isso)
  ...

Imutáveis (copiados)
  bool
  int
  float
  tuple
  str
  ...
"""
from __future__ import annotations
from copy import deepcopy


class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.addresses = []

    def __str__(self):
        attr = ', '.join(
            [f'{k} = {v}' for k, v in self.__dict__.items()]
        )
        class_name = type(self).__name__
        return f'{class_name}: ({attr})'

    def __repr__(self):
        return self.__str__()

    def add_address(self, address: Address):
        self.addresses.append(address)

    def clone(self):
        return deepcopy(self)


class Address:
    def __init__(self, street, number):
        self.street = street
        self.number = number

    def __str__(self):
        attr = ', '.join(
            [f'{k} = {v}' for k, v in self.__dict__.items()]
        )
        class_name = type(self).__name__
        return f'{class_name}: ({attr})'

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    luiz = Person('Luiz', 'Miranda')
    endereco_luiz = Address('Av. Brasil', '124B')
    luiz.add_address(endereco_luiz)

    esposa_luiz = luiz.clone()
    esposa_luiz.firstname = 'Leticia'

    print(luiz)
    print(esposa_luiz)
