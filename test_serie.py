# Test componentes en serie

from componentes import Resistencia, CircuitoSerie

resistencias = [Resistencia(20), Resistencia(60), Resistencia(40)]

c = CircuitoSerie(resistencias, 6)

print(c)
