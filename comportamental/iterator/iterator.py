"""
Iterator é um padrão comportamental que tem a
intenção de fornecer um meio de acessar,
sequencialmente, os elementos de um objeto
agregado sem expor sua representação subjacente.

- Uma coleção deve fornecer um meio de acessar
    seus elementos sem expor sua estrutura interna
- Uma coleção pode ter maneiras e percursos diferentes
    para expor seus elementos
- Você deve separar a complexidade dos algoritmos
    de iteração da coleção em si

A ideia principal do padrão é retirar a responsabilidade
de acesso e percurso de uma coleção, delegando tais
tarefas para um objeto iterador.
"""
from collections.abc import Iterator, Iterable
from typing import Any


class MyIterator(Iterator):
    def __init__(self, collection: list[Any]) -> None:
        self._collection = collection
        self._index = 0

    def __next__(self):
        try:
            item = self._collection[self._index]
            self._index += 1
            return item

        except IndexError:
            raise StopIteration


class ReverseIterator(Iterator):
    def __init__(self, collection: list[Any]) -> None:
        self._collection = collection
        self._index = -1

    def __next__(self):
        try:
            item = self._collection[self._index]
            self._index -= 1
            return item

        except IndexError:
            raise StopIteration


class MyList(Iterable):
    def __init__(self) -> None:
        self._items: list[Any] = []
        self._my_iterator = MyIterator(self._items)
        self._reverse_iterator = ReverseIterator(self._items)

    def add(self, value: Any) -> None:
        self._items.append(value)

    def reverse_iterator(self) -> Iterator:
        return self._reverse_iterator

    def __iter__(self) -> Iterator:
        return self._my_iterator

    def __str__(self) -> str:
        return f'{type(self).__name__} ({self._items})'


if __name__ == '__main__':
    minha_lista = MyList()
    minha_lista.add('Luiz')
    minha_lista.add('Maria')
    minha_lista.add('Edu')

    print(minha_lista)
    for value in minha_lista.reverse_iterator():
        print(value)
