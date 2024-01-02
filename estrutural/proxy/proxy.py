"""
O Proxy é um padrão de projeto estrutural que tem a
intenção de fornecer um objeto substituto que atua
como se fosse o objeto real que o código cliente
gostaria de usar.
O proxy receberá as solicitações e terá controle
sobre como e quando repassar tais solicitações ao
objeto real.

Com base no modo como o proxies são usados,
nós os classificamos como:

- Proxy Virtual: controla acesso a recursos que podem
ser caros para criação ou utilização.
- Proxy Remoto: controla acesso a recursos que estão
em servidores remotos.
- Proxy de proteção: controla acesso a recursos que
possam necessitar autenticação ou permissão.
- Proxy inteligente: além de controlar acesso ao
objeto real, também executa tarefas adicionais para
saber quando e como executar determinadas ações.

Proxies podem fazer várias coisas diferentes:
criar logs, autenticar usuários, distribuir serviços,
criar cache, criar e destruir objetos, adiar execuções
e muito mais...
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from time import sleep


class IUser(ABC):
    # Subject Interface
    firstname: str
    lastname: str

    @abstractmethod
    def get_addresses(self) -> list[dict]: pass

    @abstractmethod
    def get_all_user_data(self) -> dict: pass


class RealUser(IUser):
    # Real subject
    def __init__(self, firstname: str, lastname: str) -> None:
        sleep(2)  # Simulando requisiçao
        self.firstname = firstname
        self.lastname = lastname

    def get_addresses(self) -> list[dict]:
        sleep(2)  # simulando requisiçao
        return [
            {'rua': 'Av. Brasil', 'numero': 444}
        ]

    def get_all_user_data(self) -> dict:
        sleep(2)  # simulando requisiçao
        return {
            'cpf': '111.111.222-22',
            'rg': 'CG1112232'
        }


class UserProxy(IUser):
    # Proxy
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname

        # Esses objetos ainda nao existem nesse ponto do codigo
        self._real_user: RealUser
        self._cached_addresses: list[dict]
        self._cached_all_user_data: dict

    def get_real_user(self) -> None:
        if not hasattr(self, '_real_user'):
            self._real_user = RealUser(self.firstname, self.lastname)

    def get_addresses(self) -> list[dict]:
        self.get_real_user()

        if not hasattr(self, '_cached_addresses'):
            self._cached_addresses = self._real_user.get_addresses()

        return self._cached_addresses

    def get_all_user_data(self) -> dict:
        self.get_real_user()

        if not hasattr(self, '_cached_all_user_data'):
            self._cached_all_user_data = self._real_user.get_all_user_data()

        return self._cached_all_user_data


if __name__ == '__main__':
    luiz = UserProxy('Luiz', 'Otavio')

    print(luiz.firstname)
    print(luiz.lastname)

    # 6 segundos
    print(luiz.get_all_user_data())
    print(luiz.get_addresses())

    # Responde instantaneamente
    print('CACHED DATA: ')
    for i in range(50):
        print(luiz.get_addresses())
