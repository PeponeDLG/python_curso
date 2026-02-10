# Librerías fundamentales para análisis de datos
import pandas as pd             # Manipulación de datos en formato tabla
import numpy as np              # Cálculos numéricos y estadísticos
import matplotlib.pyplot as plt # Visualización básica (gráficos)
import seaborn as sns           # Visualización avanzada y estética
import os                       # Operaciones con archivos y rutas

# Cargar el archivo listings.csv descargado de Inside Airbnb
df = pd.read_csv('listings.csv')

# Vista preliminar de los datos (dos primeras líneas)
print(df.head(2))
print("="*100)

# Información general del DataFrame
print(df.info())
print("="*100)

# Estadísticas descriptivas de las variables numéricas
print(df.describe())
print("="*100)

# Selección de columnas numéricas
numeric_columns = df.select_dtypes(include=[np.number]).columns

# Visualización con histogramas
n = len(numeric_columns)
nrows = 3
ncols = min(n, 3)

fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(15, 5*nrows))
fig.suptitle('Distribución de Variables Numéricas', fontsize=16)
axes = axes.flatten()

for i, col in enumerate(numeric_columns[:len(axes)]):
    ax = axes[i]
    df[col].hist(ax=ax, bins=50, edgecolor='black')
    ax.set_title(f'Distribución de {col}')
    ax.set_xlabel(col)
    ax.set_ylabel('Frecuencia')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

# Conversión de variables categóricas
df['neighbourhood'] = df['neighbourhood'].astype('category')
df['room_type'] = df['room_type'].astype('category')

# Conteo de valores nulos
print("Valores perdidos por columna:")
print(df.isna().sum())

# Porcentaje de valores perdidos
print("Porcentaje de valores perdidos:")
print(df.isna().mean().round(2))

# Eliminación de columnas con más del 50% de valores nulos
df = df.loc[:, df.isna().mean() < 0.5]

# Imputación de valores numéricos con la media
clean_numeric_columns = df.select_dtypes(include=[np.number]).columns
df[clean_numeric_columns] = df[clean_numeric_columns].fillna(df[clean_numeric_columns].mean())

# Cálculo de límites IQR
Q1 = df['price'].quantile(0.25)
Q3 = df['price'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
 
# Visualización con boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(x=df['price'])
plt.title('Boxplot de precios con outliers')
plt.show()

# Filtrado de datos sin outliers
df_without_outliers = df[(df['price'] >= lower_bound) & (df['price'] <= upper_bound)]

# Matriz de correlación
correlation = df.select_dtypes(include=[np.number]).corr()

# Mapa de calor
plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0, square=True, linewidths=.5, cbar_kws={"shrink": .5})
plt.title('Matriz de correlación entre variables numéricas')
plt.show()

# Generación de informe con YData Profiling
from ydata_profiling import ProfileReport

report = ProfileReport(df, title='Informe EDA Airbnb Barcelona')
report.to_file('reporte_airbnb_barcelona.html')
