import pandas as pd
import matplotlib.pyplot as plt
import os
from os.path import exists

exists('datos_procesados.csv')
True
if not os.path.exists("datos_procesados.csv"):
    raise FileNotFoundError("El archivo no se encuentra descargado, ejecute el script parte6")

df = pd.read_csv("datos_procesados.csv")

anemia_count = df['anaemia'].value_counts()
diabetes_count = df['diabetes'].value_counts()
smoking_count = df['smoking'].value_counts()
death_count = df['DEATH_EVENT'].value_counts()

plt.figure(figsize=(12, 3))

plt.subplot(1, 4, 1)
plt.pie(anemia_count, labels=['No', 'Si'], autopct='%1.1f%%', startangle=90, colors=['#DEA9A9', '#A2E9C8'])
plt.title('Anémicos')

plt.subplot(1, 4, 2)
plt.pie(diabetes_count, labels=['No', 'Si'], autopct='%1.1f%%', startangle=90, colors=['#DEA9A9', '#A2E9C8'])
plt.title('Diabéticos')

plt.subplot(1, 4, 3)
plt.pie(smoking_count, labels=['No', 'Si'], autopct='%1.1f%%', startangle=90, colors=['#DEA9A9', '#A2E9C8'])
plt.title('Fumadores')

plt.subplot(1, 4, 4)
plt.pie(death_count, labels=['No', 'Si'], autopct='%1.1f%%', startangle=90, colors=['#DEA9A9', '#A2E9C8'])
plt.title('Muertos')

plt.tight_layout()
plt.show()