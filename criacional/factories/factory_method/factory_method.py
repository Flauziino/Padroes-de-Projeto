"""
Factory method é um padrão de criação que permite definir uma interface para
criar objetos, mas deixa as subclasses decidirem quais objetos criar. O
Factory method permite adiar a instanciação para as subclasses, garantindo o
baixo acoplamento entre classes.
"""
from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:
        pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo buscando cliente...')


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro popular buscando cliente...')


class Moto(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto buscando cliente...')


class MotoLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto de luxo buscando cliente...')


class VeiculoFactory(ABC):
    def __init__(self, tipo: str):
        self.carro = self.get_carro(tipo)

    @staticmethod
    @abstractmethod
    def get_carro(tipo: str) -> Veiculo:
        pass

    def buscar_cliente(self):
        self.carro.buscar_cliente()


class ZonaNorteVeiculoFactory(VeiculoFactory):

    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        if tipo == 'moto':
            return Moto()
        if tipo == 'moto de luxo':
            return MotoLuxo()
        assert 0, 'Veiculo nao existe'
        raise AssertionError


class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'popular':
            return CarroPopular()
        if tipo == 'moto':
            return Moto()
        assert 0, 'Veiculo nao existe'
        raise AssertionError


if __name__ == '__main__':
    from random import choice
    veiculos_disponiveis_zona_norte = [
        'luxo', 'popular', 'moto', 'moto de luxo'
    ]

    print('='*50)
    for i in range(10):
        carro = ZonaNorteVeiculoFactory(
            choice(
                veiculos_disponiveis_zona_norte
                )
            )
        carro.buscar_cliente()

    print('='*50)

    veiculos_disponiveis_zona_sul = ['popular', 'moto']

    for i in range(12):
        carro2 = ZonaSulVeiculoFactory(
            choice(
                veiculos_disponiveis_zona_sul
                )
            )
        carro2.buscar_cliente()
    print('='*50)
