from componentes import Resistencia


class Circuito:
    """Clase generica para representar un circuito"""

    def __init__(self):
        self.elementos: list[Circuito | Resistencia]
        self.resistencia: float
        self.corriente: float
        self.voltaje: float

    def calcular_resistencia(self) -> float:
        """Calcula la resistencia del circuito en ohmnios"""
        ...

    def calcular_corriente(self) -> float:
        """Calcula la corriente del circuito en amperios"""
        ...

    def calcular_voltaje(self) -> float:
        """Calcula el voltaje del circuito en voltios"""
        ...
