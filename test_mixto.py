from componentes import CircuitoParalelo, CircuitoSerie, Resistencia

# Como los circuitos están en paralelo el voltaje de cada uno es el mismo
r1 = [Resistencia(1), Resistencia(4)]
c1 = CircuitoSerie(r1, 300)

r2 = [Resistencia(10), Resistencia(10)]
c2 = CircuitoSerie(r2, 300)

c = CircuitoParalelo([c1, c2], 300)

print("# Circuito 1")
print(c1)
print("# Circuito 2")
print(c2)
print("# Circuito global")
print(c)
