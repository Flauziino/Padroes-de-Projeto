"""
Strategy é um padrão de projeto comportamental que tem
a intenção de definir uma família de algoritmos,
encapsular cada uma delas e torná-las intercambiáveis.
Strategy permite que o algorítmo varie independentemente
dos clientes que o utilizam.

Princípio do aberto/fechado (Open/closed principle)
Entidades devem ser abertas para extensão, mas fechadas para modificação
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class StringReprMixin:
    def __str__(self):
        attr = ', '.join(
            [f'{k} = {v}' for k, v in self.__dict__.items()]
        )
        class_name = type(self).__name__
        return f'{class_name}: ({attr})'

    def __repr__(self):
        return self.__str__()


class Order(StringReprMixin):
    def __init__(self, total: float, discount: DiscountStrategy):
        self._total = total
        self._discount = discount

    @property
    def total(self):
        return self._total

    @property
    def total_with_discount(self):
        return self._discount.calculate(self.total)


class DiscountStrategy(ABC, StringReprMixin):
    @abstractmethod
    def calculate(self, value: float) -> float: pass


class TwentyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value * 0.8


class FiftyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value * 0.5


class FifteenPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value * 0.85


class TenPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value * 0.90


class FivePercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value * 0.95


class NoDiscount(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value


class CustemDiscount(DiscountStrategy):
    def __init__(self, discount):
        self.discount = discount / 100

    def calculate(self, value: float) -> float:
        return value - (value * self.discount)


if __name__ == '__main__':
    twenty_percent = TwentyPercent()
    fifty_percent = FiftyPercent()
    fifteen_percent = FifteenPercent()
    ten_percent = TenPercent()
    five_percent = FivePercent()

    order = Order(1000, twenty_percent)
    order2 = Order(1000, fifty_percent)
    order3 = Order(1000, fifteen_percent)
    order4 = Order(1000, ten_percent)
    order5 = Order(1000, five_percent)

    print(order.total, order.total_with_discount)
    print(order2.total, order2.total_with_discount)
    print(order3.total, order3.total_with_discount)
    print(order4.total, order4.total_with_discount)
    print(order5.total, order5.total_with_discount)
