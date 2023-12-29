"""
Mediator é um padrão de projeto comportamental
que tem a intenção de definir um objeto que
encapsula a forma como um conjunto de objetos
interage. O Mediator promove o baixo acoplamento
ao evitar que os objetos se refiram uns aos
outros explicitamente e permite variar suas
interações independentemente.
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Colleague(ABC):
    def __init__(self):
        self.name: str

    @abstractmethod
    def broadcast(self, msg: str):
        pass

    @abstractmethod
    def direct(self, msg: str):
        pass


class Person(Colleague):
    def __init__(self, name: str, mediator: Mediator) -> None:
        self.name = name
        self.mediator = mediator

    def broadcast(self, msg: str):
        self.mediator.broadcast(self, msg)

    def send_direct(self, receiver: str, msg: str) -> None:
        self.mediator.direct(self, receiver, msg)

    def direct(self, msg: str):
        print(msg)


class Mediator(ABC):
    @abstractmethod
    def broadcast(self, colleague: Colleague, msg: str) -> None:
        pass

    @abstractmethod
    def direct(self, sender: Colleague, receiver: str, msg: str) -> None:
        pass


class Chatroom(Mediator):
    # Concrete mediator
    def __init__(self):
        self.colleagues: list[Colleague] = []

    def is_colleague(self, colleague: Colleague) -> bool:
        return colleague in self.colleagues

    def add(self, colleague: Colleague) -> None:
        if not self.is_colleague(colleague):
            self.colleagues.append(colleague)

    def remove(self, colleague: Colleague) -> None:
        if self.is_colleague(colleague):
            self.colleagues.remove(colleague)

    def broadcast(self, colleague: Colleague, msg: str) -> None:
        if not self.is_colleague(colleague):
            return

        print(f'{colleague.name} disse: {msg}')

    def direct(self, sender: Colleague, receiver: str, msg: str) -> None:
        if not self.is_colleague(sender):
            return

        receiver_obj: list[Colleague] = [
            colleague for colleague in self.colleagues
            if colleague.name == receiver
        ]

        if not receiver_obj:
            return

        receiver_obj[0].direct(
            f'{sender.name} para {receiver_obj[0].name}: {msg}'
        )


if __name__ == '__main__':
    chat = Chatroom()

    p1 = Person('Joao', chat)
    p2 = Person('Helena', chat)
    p3 = Person('Edu', chat)
    p4 = Person('Carla', chat)
    p5 = Person('Marcia', chat)

    chat.add(p1)
    chat.add(p2)
    chat.add(p3)
    chat.add(p4)
    chat.add(p5)

    p1.broadcast('Ola mundo')
    p5.broadcast('Oi?')
    print()

    p1.direct('heeey')
    p1.send_direct('Marcia', 'Marcia, ta ai?')
