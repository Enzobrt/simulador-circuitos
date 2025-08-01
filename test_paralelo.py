# Test componentes en paralelo

from componentes import Resistencia, CircuitoParalelo

def test_sencillo():
    # Test para un circuito sencillo con una sola resistencia
    resistencias = [Resistencia(30)]
    c = CircuitoParalelo(resistencias, 6)
    assert c.calcular_resistencia() == 30
    assert c.calcular_voltaje() == 6
    assert c.calcular_corriente() == 0.2

def test_varias_r():
    # Test para un circuito con varias resistencias
    resistencias = [Resistencia(10), Resistencia(15), Resistencia(30)]
    c = CircuitoParalelo(resistencias, 90)
    assert c.calcular_resistencia() == 5
    assert c.calcular_voltaje() == 90
    assert c.calcular_corriente() == 18

