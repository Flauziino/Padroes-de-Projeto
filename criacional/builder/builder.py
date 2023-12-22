"""
Builder é um padrão de criação que tem a intenção
de separar a construção de um objeto complexo
da sua representação, de modo que o mesmo processo
de construção possa criar diferentes representações.

Builder te da a possibilidade de criar objetos passo-a-passo
e isso já é possível no Python sem este padrão.

Geralmente o builder aceita o encadeamento de métodos
(method chaining).
"""
from abc import ABC, abstractmethod


class User:
    def __init__(self):
        self.firstname = None
        self.lastname = None
        self.age = None
        self.phone = []
        self.adresses = []

    def __str__(self):
        attr = ', '.join(
            [f'{k} = {v}' for k, v in self.__dict__.items()]
        )
        class_name = type(self).__name__
        return f'{class_name}: ({attr})'

    def __repr__(self):
        return self.__str__()


class IUserBuilder(ABC):
    @property
    @abstractmethod
    def result(self): pass

    @abstractmethod
    def add_firstname(self, firstname): pass

    @abstractmethod
    def add_lastname(self, lastname): pass

    @abstractmethod
    def add_age(self, age): pass

    @abstractmethod
    def add_phone(self, phone): pass

    @abstractmethod
    def add_adress(self, adress): pass


class UserBuilder(IUserBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._result = User()

    @property
    def result(self):
        return_data = self._result
        self.reset()
        return return_data

    def add_firstname(self, firstname):
        self._result.firstname = firstname
        return self

    def add_lastname(self, lastname):
        self._result.lastname = lastname
        return self

    def add_age(self, age):
        self._result.age = age
        return self

    def add_phone(self, phone):
        phone_number = phone
        self._result.phone.append(phone_number)
        return self

    def add_adress(self, adress):
        adr = adress
        self._result.adresses.append(adr)
        return self


class UserDirector:
    def __init__(self, builder):
        self._builder: UserBuilder = builder

    def with_age(self, firstname, lastname, age):
        self._builder.add_firstname(firstname)
        self._builder.add_lastname(lastname)
        self._builder.add_age(age)
        return self._builder.result

    # Utilizando encadeamento de methodos
    def with_adress(self, firstname, lastname, adress):
        self._builder.add_firstname(firstname)\
            .add_lastname(lastname)\
            .add_adress(adress)
        return self._builder.result

    def with_phone(self, firstname, lastname, phone):
        self._builder.add_firstname(firstname)\
            .add_lastname(lastname)\
            .add_phone(phone)
        return self._builder.result


if __name__ == '__main__':
    user_builder = UserBuilder()
    user_director = UserDirector(user_builder)

    user1 = user_director.with_age('Carlos', 'Eduardo', 35)
    print(user1)
    print()

    user2 = user_director.with_adress('Kadu', 'Ribeiro', 'R. Argentina, 25')
    print(user2)
    print()

    user3 = user_director.with_phone('Maria', 'Pereira', 55223112)
    print(user3)
