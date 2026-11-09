print("Christian Garcia Jimenez Nc = 0068")
print("Fecha = viernes/06/Noviembre/11/2026")

# Paso 1: Importar librerías
import pandas as pd
import numpy as np

# Paso 2: Crear el DataFrame de muestra
datos = {
    "Cliente": ["Usuario1", "Usuario2", "Usuario3", "Usuario4", "Usuario5", "Usuario6"],
    "Antiguedad_Meses": [2, 36, 12, 5, 48, 1],
    "Gasto_Mensual": [29.99, 89.99, 59.99, 19.99, 110.00, 49.99],
    "Cancela_Servicio": [True, False, False, True, False, True]
}
df = pd.DataFrame(datos)
print(df)

# Paso 3: Agrupación básica (GroupBy)
print("+-+-+-+-Agrupar por una sola columna-+-+-+-+-+--+")
agrupar = df.groupby('Cancela_Servicio')
print(agrupar)

print("+-+-+-+-Agregación-+-+-+-+-+-+")
# Gasto promedio según el estado de cancelación
print(agrupar['Gasto_Mensual'].mean())
print("+-+-+-+- por nivel de rango máximo -+-+-+-+")
# Antigüedad máxima en cada grupo de cancelación
print(agrupar['Antiguedad_Meses'].max())

print("+-+-+-Christian Garcia Jimenez Nc = 0068 +-+-+- Segunda parte +-+-+-+-+-+-+- ")
print("Agregaciones múltiples")
print("mean --> promedio.  sum --> suma.  max ---> máximo. min ---> mínimo")

# Aplicar múltiples funciones de agregación al gasto mensual
# Se renombran las funciones en el diccionario/lista para que la salida esté en español
resultado_agregado = agrupar['Gasto_Mensual'].agg(
    promedio='mean', 
    suma='sum', 
    maximo='max', 
    minimo='min'
)
print(resultado_agregado)

print("Agrupación por varias columnas")
print("Agrega columnas al dataframe")
print(" columna --> equipo")

# Crear una columna condicional de equipo (antigüedad mayor a 12 meses)
df['Equipo'] = df['Antiguedad_Meses'] > 12

# CORRECCIÓN: Se utiliza 'Equipo' en lugar de 'Segmento' para coincidir con la columna creada
agrupado_multiple = df.groupby(['Cancela_Servicio', 'Equipo'])['Gasto_Mensual'].mean()
print(agrupado_multiple)