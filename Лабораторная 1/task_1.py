# TODO Написать 3 класса с документацией и аннотацией типов
from abc import ABC, abstractmethod
class HeatingSystem(ABC):
    """
    Класс системы отопления.

    Атрибуты:
        power (float): Мощность системы отопления в киловаттах (кВт).
        energy_source (str): Источник энергии (газ, электричество, твердое топливо).
    """
    def __init__(self, power: float, energy_source: str):
        if power <= 0:
            raise ValueError("Мощность должна быть положительным числом.")
        if energy_source not in ["газ", "электричество", "твердое топливо"]:
            raise ValueError("Недопустимый источник энергии.")
        self.power = power
        self.energy_source = energy_source

    @abstractmethod
    def start_heating(self) -> None:
        """Запустить систему отопления."""
        ...

    @abstractmethod
    def stop_heating(self) -> None:
        """Остановить систему отопления."""
        ...


class WaterSupplySystem(ABC):
    """
      Атрибуты:
        pressure (float): Давление воды в системе в барах.
        source (str): Источник воды (городская сеть, скважина).
    """

    def __init__(self, pressure: float, source: str):
        if pressure <= 0:
            raise ValueError("Давление воды должно быть положительным числом.")
        if source not in ["городская сеть", "скважина"]:
            raise ValueError("Недопустимый источник воды.")
        self.pressure = pressure
        self.source = source

    @abstractmethod
    def start_pump(self) -> None:
        """Запустить насос для подачи воды."""
        ...

    @abstractmethod
    def stop_pump(self) -> None:
        """Остановить насос."""
        ...


class ElectricalSystem(ABC):
    """
     Атрибуты:
        voltage (float): Напряжение сети в вольтах.
        max_load (float): Максимальная нагрузка в киловаттах (кВт).
    """

    def __init__(self, voltage: float, max_load: float):
        if voltage <= 0:
            raise ValueError("Напряжение должно быть положительным числом.")
        if max_load <= 0:
            raise ValueError("Максимальная нагрузка должна быть положительным числом.")
        self.voltage = voltage
        self.max_load = max_load

    @abstractmethod
    def switch_on(self) -> None:
        """Включить систему электроснабжения."""
        ...

    @abstractmethod
    def switch_off(self) -> None:
        """Выключить систему электроснабжения."""
        ...
