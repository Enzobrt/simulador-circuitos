# Test componentes en paralelo

from componentes import Resistencia, CircuitoParalelo

resistencias = [Resistencia(9), Resistencia(18), Resistencia(30)]

c = CircuitoParalelo(resistencias, 90)

print(c)
