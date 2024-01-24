import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
from sklearn.manifold import TSNE
import os
from os.path import exists

exists('datos_procesados.csv')
True
if not os.path.exists("datos_procesados.csv"):
    raise FileNotFoundError("El archivo no se encuentra descargado, ejecute el script parte6")

df = pd.read_csv("datos_procesados.csv")

# Eliminar las columnas objetivo y categoria_edad

dfreduce = df.drop(columns=["DEATH_EVENT", "edad_categoria"]).copy()

# Convertir el DataFrame a un array NumPy
X = dfreduce.values

# Exportar el array unidimensional de la columna objetivo
y = df["DEATH_EVENT"].values

# Ejecutar la reducción de dimensionalidad
X_embedded = TSNE(
    n_components=3,
    learning_rate="auto",
    init="random",
    perplexity=3,
).fit_transform(X)

# Crear el gráfico de dispersión 3D
data = {'Dim_1': X_embedded[:, 0], 'Dim_2': X_embedded[:, 1], 'Dim_3': X_embedded[:, 2], 'DEATH_EVENT': y}
df = pd.DataFrame(data)
color_map = {0: 'Muerto', 1: 'Vivo'}
df['Color'] = df['DEATH_EVENT'].map(color_map)


fig = px.scatter_3d(df, x='Dim_1', y='Dim_2', z='Dim_3', color='Color', 
                    title='Gráfico de Dispersión 3D con Colores por Clase')


fig.update_traces(marker=dict(size=4, opacity=0.8))
fig.show()