# 1. Leer el archivo
import pandas as pd  # ← instalar

datos = pd.read_csv("resistencias.csv")
print(datos)

# 2. almacenar las resistencias y baterias
resistencias = datos.loc[
    datos["elemento"] == "resistencia", ["nombre", "valor"]]

baterias = datos.loc[
    datos["elemento"] == "bateria", ["nombre", "valor"]]


# 3. recorrer los datos y hacer los calculos
r_total = resistencias["valor"].sum()
v_total = baterias["valor"].sum()
corriente = v_total / r_total

print(f"Resistencia total: {r_total} Ohm")
print(f"Corriente del circuito: {corriente} A")
print(f"Voltaje total: {v_total} V")
print()

# Añadir columan con voltaje para cada resistenca
# Añadir columan con corriente para cada resistenca
print(resistencias)


# 4. Imprimir resultados
# recorrer la tabla resistencias
# print(f"Resistenca nombre, R: 4 Ohm, V: 10 V, I: 10 A")
