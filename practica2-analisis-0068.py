print("Christian Garcia Jimenez Nc = 0068")
print("Fecha = viernes/06/Noviembre/11/2026")
# Paso 1: Importar librerías
import pandas as pd
import numpy as np

# Paso 2: Crear el DataFrame de muestra
data = {
    "Cliente": ["User1", "User2", "User3", "User4", "User5", "User6"],
    "Antiguedad_Meses": [2, 36, 12, 5, 48, 1],
    "Gasto_Mensual": [29.99, 89.99, 59.99, 19.99, 110.00, 49.99],
    "Cancela_Servicio": [True, False, False, True, False, True]
}
df = pd.DataFrame(data)
print(df)

# Paso 3: Agrupación básica (GroupBy)
# Agrupar por una sola columna
agrupar = df.groupby('Cancela_Servicio')
print(agrupar)

# Agregación
# Gasto promedio según el estado de cancelación
print(agrupar['Gasto_Mensual'].mean())

# Antigüedad máxima en cada grupo de cancelación
print(agrupar['Antiguedad_Meses'].max())



