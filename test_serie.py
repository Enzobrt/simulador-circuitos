# Test componentes en serie

from componentes import Resistencia, CircuitoSerie

def test_sencillo():
    # Test para un circuito sencillo con una sola resistencia
    resistencias = [Resistencia(30)]
    c = CircuitoSerie(resistencias, 6)
    assert c.calcular_resistencia() == 30
    assert c.calcular_voltaje() == 6
    assert c.calcular_corriente() == 0.2


def test_varias_r():
    # Test para un circuito con varias resistencias
    resistencias = [Resistencia(20), Resistencia(40), Resistencia(60)]
    c = CircuitoSerie(resistencias, 6)
    assert c.calcular_resistencia() == 120
    assert c.calcular_voltaje() == 6
    assert c.calcular_corriente() == 0.05
