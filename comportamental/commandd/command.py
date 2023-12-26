"""
Command tem intenção de encapsular uma solicitação como
um objeto, desta forma permitindo parametrizar clientes com diferentes
solicitações, enfileirar ou fazer registro (log) de solicitações e suportar
operações que podem ser desfeitas.

É formado por um cliente (quem orquestra tudo), um invoker (que invoca as
solicitações), um ou vários objetos de comando (que fazem a ligação entre o
receiver e a ação a ser executada) e um receiver (o objeto que vai executar a
ação no final).
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Light:
    # Receiver -> Luz Inteligente

    def __init__(self, name: str, room_name: str) -> None:
        self.name = name
        self.room_name = room_name
        self.color = 'Default color'

    def on(self) -> None:
        print(f'A {self.name} no {self.room_name} esta LIGADA')

    def off(self) -> None:
        print(f'A {self.name} no {self.room_name} esta DESLIGADA')

    def change_color(self, color: str) -> None:
        self.color = color
        print(f'A {self.name} no {self.room_name} esta {self.color}')


class ICommand(ABC):
    # Interface de comando

    @abstractmethod
    def execute(self) -> None: pass

    @abstractmethod
    def undo(self) -> None: pass


class LightOnCommand(ICommand):
    # Comando concreto

    def __init__(self, light: Light) -> None:
        self.light = light

    def execute(self) -> None:
        self.light.on()

    def undo(self) -> None:
        self.light.off()


class LightChangeColor(ICommand):
    # Comando concreto

    def __init__(self, light: Light, color: str) -> None:
        self.light = light
        self.color = color
        self._old_color = self.light.color

    def execute(self) -> None:
        self._old_color = self.light.color
        self.light.change_color(self.color)

    def undo(self) -> None:
        self.light.change_color(self._old_color)


class RemoteController:
    # Invoker

    def __init__(self) -> None:
        self._buttons: dict[str, ICommand] = {}
        self._undos: list[tuple[str, str]] = []

    def button_add_command(self, name: str, command: ICommand) -> None:
        self._buttons[name] = command

    def button_execute(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].execute()
            self._undos.append((name, 'execute'))

    def button_undo(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].undo()
            self._undos.append((name, 'undo'))

    def global_undo(self):
        if not self._undos:
            return None

        button_name, action = self._undos[-1]

        if action == 'execute':
            self._buttons[button_name].undo()
        else:
            self._buttons[button_name].execute()

        self._undos.pop()


if __name__ == '__main__':
    bedroom_light = Light('Luz', 'Quarto')
    bathroom_light = Light('Luz', 'Banheiro')

    bedroom_light_on = LightOnCommand(bedroom_light)
    bedroom_light_blue = LightChangeColor(bedroom_light, 'Azul')
    bathroom_light_on = LightOnCommand(bathroom_light)

    remote = RemoteController()
    remote.button_add_command('first_button', bedroom_light_on)
    remote.button_add_command('second_button', bedroom_light_blue)

    remote.button_execute('first_button')
    remote.button_undo('first_button')

    remote.button_execute('second_button')
    remote.button_undo('second_button')

    print()
    print()

    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
