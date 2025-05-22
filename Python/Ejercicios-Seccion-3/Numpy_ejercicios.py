import numpy as np

# 1. Crear un array NumPy de 10 ceros
ejer_1 = np.zeros(10)
print("1:", ejer_1)

# 2. Crear un array de 10 unos
ejer_2 = np.ones(10)
print("2:", ejer_2)

# 3. Crear un array de 10 cincos
ejer_3 = np.full(10, 5)
print("3:", ejer_3)

# 4. Crear un array con valores del 10 al 50
ejer_4 = np.arange(10, 51)
print("4:", ejer_4)

# 5. Crear una matriz de 3x3 con valores del 0 al 8
ejer_5 = np.arange(9).reshape(3, 3)
print("5:\n", ejer_5)

# 6. Crear una matriz identidad de 4x4
ejer_6 = np.eye(4)
print("6:\n", ejer_6)

# 7. Generar un número aleatorio entre 0 y 1
ejer_7 = np.random.rand()
print("7:", ejer_7)

# 8. Generar un array de 10 números aleatorios siguiendo una distribución normal
ejer_8 = np.random.randn(10)
print("8:", ejer_8)

# 9. Crear una matriz de 5x5 con valores aleatorios entre 0 y 100
ejer_9 = np.random.randint(0, 100, (5, 5))
print("9:\n", ejer_9)

# 10. Obtener la media de un array dado
ejer_10 = np.array([10, 20, 30, 40, 50])
media = np.mean(ejer_10)
print("10: Media =", media)

# 11. Obtener la suma de todos los elementos de una matriz
ejer_11 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
suma = np.sum(ejer_11)
print("11: Suma =", suma)

# 12. Obtener los valores máximos y mínimos de una matriz
max_val = np.max(ejer_11)
min_val = np.min(ejer_11)
print("12: Max =", max_val, ", Min =", min_val)

# 13. Crear una matriz de 5x5 con valores del 1 al 25 y extraer la diagonal
ejer_13 = np.arange(1, 26).reshape(5, 5)
diagonal = np.diag(ejer_13)
print("13: Diagonal =", diagonal)

# 14. Filtrar valores mayores a 50 en un array aleatorio
ejer_14 = np.random.randint(0, 100, 20)
filtrado = ejer_14[ejer_14 > 50]
print("14: Filtrado =", filtrado)

# 15. Multiplicar dos matrices de 3x3
mat1 = np.random.randint(1, 10, (3, 3))
mat2 = np.random.randint(1, 10, (3, 3))
producto = np.dot(mat1, mat2)
print("15: Producto\n", producto)
