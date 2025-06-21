"""
Modulo para simular los circuitos
"""

#
from .resistencia import Resistencia
from .circuito import Circuito
from .circuito_serie import CircuitoSerie
from .circuito_paralelo import CircuitoParalelo


__all__ = ["Resistencia", "Circuito", "CircuitoSerie", "CircuitoParalelo"]
