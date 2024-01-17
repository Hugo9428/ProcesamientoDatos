import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import os
from os.path import exists

exists('datos_procesados.csv')
True
if not os.path.exists("datos_procesados.csv"):
    raise FileNotFoundError("El archivo no se encuentra descargado, ejecute el script parte6")

df = pd.read_csv("datos_procesados.csv")
df['age'] = pd.to_numeric(df['age'])
cantidad_adultos = df.loc[df["edad_categoria"] == "Adulto"].shape[0]
cantidad_adulto_mayor = df.loc[df["edad_categoria"] == "Adulto mayor"].shape[0]
fig = go.Figure(data=[go.Bar(
    x=["Adulto", "Adulto mayor"],
    y=[cantidad_adultos, cantidad_adulto_mayor],
    marker_color=["blue", "red"]
)])

# Personalizar el diseño del gráfico
fig.update_layout(
    title="Cantidad de pacientes por categoría de edad",
    xaxis_title="Categoría de edad",
    yaxis_title="Cantidad"
)

# Mostrar el gráfico
fig.show()


male_data = df[df['sex'] == 1]  # 1 representa a hombres
female_data = df[df['sex'] == 0]

# Calcular la cantidad de anémicos, diabéticos, fumadores y muertos por género
male_counts = [
    male_data['anaemia'].sum(),
    male_data['diabetes'].sum(),
    male_data['smoking'].sum(),
    male_data['DEATH_EVENT'].sum()
]

female_counts = [
    female_data['anaemia'].sum(),
    female_data['diabetes'].sum(),
    female_data['smoking'].sum(),
    female_data['DEATH_EVENT'].sum()
]

categories = ['Anémicos', 'Diabéticos', 'Fumadores', 'Muertos']


bar_width = 0.35
index = range(len(categories))

plt.bar(index, male_counts, bar_width, label='Hombres', color = 'blue')
plt.bar([i + bar_width for i in index], female_counts, bar_width, label='Mujeres', color = 'red')


plt.xlabel('Categorías')
plt.ylabel('Cantidad')
plt.title('Histograma agrupado por sexo')
plt.xticks([i + bar_width / 2 for i in index], categories)
plt.legend()
plt.yticks([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
plt.tight_layout()
plt.show()
