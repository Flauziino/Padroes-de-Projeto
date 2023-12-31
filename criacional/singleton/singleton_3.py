# class Meta(type):
#     def __call__(cls, *args, **kwargs):
#         return super().__call__(*args, **kwargs)


# class Pessoa(metaclass=Meta):
#     def __new__(cls, *args, **kwargs):
#         return super().__new__(cls)

#     def __init__(self, nome):
#         self.nome = nome

#     def __call__(self):
#         print('Call chamado')


# if __name__ == '__main__':
#     p1 = Pessoa('Luiz')
#     p1()
#     print(p1.nome)
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class AppSettings(metaclass=Singleton):
    def __init__(self):
        print('Ola')
        self.tema = 'O tema escuro'
        self.font = '18px'


if __name__ == '__main__':
    as1 = AppSettings()
    as1.tema = 'O tema claro'
    print(as1.tema)

    as2 = AppSettings()
    print(as1.tema)
    print(as2.tema)
