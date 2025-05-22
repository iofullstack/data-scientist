import pandas as pd
import numpy as np

# 1. Crear un DataFrame simple
data = {'Nombre': ['Ana', 'Luis', 'Carlos', 'Marta'], 'Edad': [23, 45, 31, 27]}
df = pd.DataFrame(data)
print("Ejercicio 1: DataFrame simple\n", df, "\n")

# 2. Cargar datos desde un diccionario y mostrar estadísticas básicas
data = {'A': np.random.randint(1, 100, 10), 'B': np.random.rand(10)}
df = pd.DataFrame(data)
print("Ejercicio 2: Estadísticas básicas\n", df.describe(), "\n")

# 3. Filtrar datos según una condición
df_filtrado = df[df['A'] > 50]
print("Ejercicio 3: Filtrado de datos\n", df_filtrado, "\n")

# 4. Agregar una nueva columna basada en otra
df['C'] = df['A'] * 2
print("Ejercicio 4: Nueva columna\n", df, "\n")

# 5. Ordenar un DataFrame por una columna
df_ordenado = df.sort_values(by='A', ascending=False)
print("Ejercicio 5: Ordenar DataFrame\n", df_ordenado, "\n")

# 6. Manejo de valores nulos
data = {'X': [1, 2, np.nan, 4], 'Y': [np.nan, 2, 3, 4]}
df = pd.DataFrame(data)
df.fillna(0, inplace=True)
print("Ejercicio 6: Manejo de valores nulos\n", df, "\n")

# 7. Agrupar datos y calcular estadísticas
data = {'Categoria': ['A', 'A', 'B', 'B', 'C'], 'Valor': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)
agrupado = df.groupby('Categoria').sum()
print("Ejercicio 7: Agrupación de datos\n", agrupado, "\n")

# 8. Aplicar funciones personalizadas a una columna
df['Valor_modificado'] = df['Valor'].apply(lambda x: x ** 2)
print("Ejercicio 8: Función personalizada\n", df, "\n")

# 9. Concatenar dos DataFrames
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Valor': [10, 20, 30]})
df2 = pd.DataFrame({'ID': [4, 5, 6], 'Valor': [40, 50, 60]})
df_concatenado = pd.concat([df1, df2])
print("Ejercicio 9: Concatenación\n", df_concatenado, "\n")

# 10. Merge de dos DataFrames
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Nombre': ['Ana', 'Luis', 'Carlos']})
df2 = pd.DataFrame({'ID': [1, 2, 4], 'Edad': [23, 45, 30]})
df_merge = pd.merge(df1, df2, on='ID', how='outer')
print("Ejercicio 10: Merge\n", df_merge, "\n")

# 11. Pivotar un DataFrame
data = {'Fecha': ['2024-01', '2024-01', '2024-02', '2024-02'], 'Categoria': ['A', 'B', 'A', 'B'], 'Ventas': [100, 200, 150, 250]}
df = pd.DataFrame(data)
df_pivot = df.pivot(index='Fecha', columns='Categoria', values='Ventas')
print("Ejercicio 11: Pivotar\n", df_pivot, "\n")

# 12. Crear una tabla dinámica
df_pivot_table = df.pivot_table(values='Ventas', index='Fecha', columns='Categoria', aggfunc=np.sum)
print("Ejercicio 12: Tabla dinámica\n", df_pivot_table, "\n")

# 13. Convertir una columna en tipo datetime
df['Fecha'] = pd.to_datetime(df['Fecha'])
print("Ejercicio 13: Convertir a datetime\n", df.dtypes, "\n")

# 14. Crear una serie de tiempo
dates = pd.date_range(start='2024-01-01', periods=10, freq='D')
series = pd.DataFrame({'Fecha': dates, 'Valores': np.random.randint(1, 100, 10)})
print("Ejercicio 14: Serie de tiempo\n", series, "\n")

# 15. Aplicar operaciones de rolling window
df_rolling = series.set_index('Fecha').rolling(window=3).mean()
print("Ejercicio 15: Rolling Window\n", df_rolling, "\n")