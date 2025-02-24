from typing import Any


class HeatingSystem:
    """
    Базовый класс для систем отопления.
    """

    def __init__(self, power: float, efficiency: float) -> None:
        """
        Конструктор класса HeatingSystem.
        :param power: Мощность системы отопления в кВт.
        :param efficiency: КПД системы отопления в процентах.
        """
        self._power = power  # Инкапсуляция мощности системы
        self.efficiency = efficiency

    def calculate_heat_output(self) -> float:
        """
        Метод для расчета эффективной тепловой мощности.
        """
        return self._power * (self.efficiency / 100)

    def __str__(self) -> str:
        return f"Система отопления: мощность {self._power} кВт, КПД {self.efficiency}%."

    def __repr__(self) -> str:
        return f"HeatingSystem(power={self._power!r}, efficiency={self.efficiency!r})"


class RadiatorHeating(HeatingSystem):
    """
    Дочерний класс, представляющий радиаторное отопление.
    """

    def __init__(self, power: float, efficiency: float, number_of_radiators: int) -> None:
        """
        Конструктор класса RadiatorHeating.
        :param power: Мощность системы отопления в кВт.
        :param efficiency: КПД системы отопления в процентах.
        :param number_of_radiators: Количество радиаторов в системе.
        """
        super().__init__(power, efficiency)
        self.number_of_radiators = number_of_radiators

    def calculate_heat_output(self) -> float:
        """
        Переопределённый метод для расчета мощности с учетом количества радиаторов.
        """
        return super().calculate_heat_output() * self.number_of_radiators

    def __str__(self) -> str:
        return f"Радиаторное отопление: {self.number_of_radiators} радиаторов, мощность {self._power} кВт, КПД {self.efficiency}%."

    def __repr__(self) -> str:
        return f"RadiatorHeating(power={self._power!r}, efficiency={self.efficiency!r}, number_of_radiators={self.number_of_radiators!r})"


if __name__ == "__main__":
    heating = HeatingSystem(10, 90)
    radiator_heating = RadiatorHeating(10, 85, 5)

    print(heating)
    print(radiator_heating)
    print(heating.calculate_heat_output())
    print(radiator_heating.calculate_heat_output())  