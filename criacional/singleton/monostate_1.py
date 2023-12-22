"""
Monostate (ou Borg) - É uma variação do Singleton proposto
por Alex Martelli que tem a intenção de garantir que o
estado do objeto seja igual para todas as instâncias.
"""


class StringReprMixin:
    def __str__(self):
        attr = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
        )
        class_name = type(self).__name__
        return f'{class_name}: ({attr})'

    def __repr__(self):
        return self.__str__()


class MonoStateSimple(StringReprMixin):
    _state = dict(
        x=10,
        y=20,
    )

    def __init__(self, nome=None, sobrenome=None):
        self.x = ''
        self.y = ''
        self.__dict__ = self._state

        if nome is not None:
            self.nome = nome

        if sobrenome is not None:
            self.sobrenome = sobrenome


if __name__ == '__main__':
    a = MonoStateSimple()
    print(a)
