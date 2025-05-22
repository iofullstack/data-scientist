import numpy as np
from random import randint
import matplotlib.pyplot as plt

# 1. Gráfico de línea simple
y = np.array([1, 3, 2, 4, 6, 5])
plt.plot(y)
plt.title("Gráfico de Línea Simple")
plt.show()

# 2. Gráfico de línea con dos series de datos
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, label='Seno')
plt.plot(x, y2, label='Coseno')
plt.legend()
plt.title("Seno y Coseno")
plt.show()

# 3. Gráfico de dispersión simple
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y, color='red')
plt.title("Gráfico de Dispersión")
plt.show()

# 4. Histograma de datos aleatorios
data = np.random.randn(1000)
plt.hist(data, bins=30, color='blue', edgecolor='black')
plt.title("Histograma de Datos Aleatorios")
plt.show()

# 5. Gráfico de barras
categorias = ['A', 'B', 'C', 'D']
valores = [3, 7, 1, 8]
plt.bar(categorias, valores, color='green')
plt.title("Gráfico de Barras")
plt.show()

# 6. Gráfico de barras horizontales
plt.barh(categorias, valores, color='purple')
plt.title("Gráfico de Barras Horizontales")
plt.show()

# 7. Gráfico de pastel
plt.pie(valores, labels=categorias, autopct='%1.1f%%', colors=['red', 'blue', 'green', 'orange'])
plt.title("Gráfico de Pastel")
plt.show()

# 8. Gráfico de áreas acumuladas
x = np.linspace(0, 10, 100)
y = np.sin(x)**2
plt.fill_between(x, y, color='cyan', alpha=0.5)
plt.title("Gráfico de Áreas Acumuladas")
plt.show()

# 9. Gráfico de líneas múltiples con estilos
y3 = np.tan(x)
plt.plot(x, y1, linestyle='dashed', label='Seno')
plt.plot(x, y2, linestyle='dotted', label='Coseno')
plt.plot(x, y3, linestyle='solid', label='Tangente')
plt.legend()
plt.title("Líneas con Diferentes Estilos")
plt.ylim(-5, 5)
plt.show()

# 10. Gráfico de cajas (boxplot)
data = [np.random.randn(100) * i for i in range(1, 5)]
plt.boxplot(data, labels=['A', 'B', 'C', 'D'])
plt.title("Gráfico de Cajas")
plt.show()

# 11. Gráfico de violín
import seaborn as sns
sns.violinplot(data=data)
plt.title("Gráfico de Violín")
plt.show()

# 12. Mapa de calor
heatmap_data = np.random.rand(10, 10)
sns.heatmap(heatmap_data, cmap='coolwarm', annot=True)
plt.title("Mapa de Calor")
plt.show()

# 13. Gráfico de dispersión con tamaño y color aleatorio
np.random.seed(19680801)
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()

# 14. Gráfico 3D de superficie
X = np.linspace(-5, 5, 50)
Y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='plasma')
plt.title("Gráfico 3D de Superficie")
plt.show()

# 15. Gráfico de líneas con anotaciones
x = np.linspace(-5, 5, 50)
y = np.sin(np.sqrt(x**2))
plt.plot(x, y, label='Seno')
plt.annotate('Máximo', xy=(np.pi/2, 1), xytext=(np.pi/2, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.title("Gráfico con Anotaciones")
plt.legend()
plt.show()
