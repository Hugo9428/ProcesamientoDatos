"""""
Una vez cargado el csv mediante el request anterior, realiza lo siguiente:
1.Verificar que no existan valores faltantes
2.Verificar que no existan filas repetidas
3.Verificar si existen valores atípicos y eliminarlos
4.Crear una columna que categorice por edades
    0-12: Niño
    13-19: Adolescente
    20-39: Jóvenes adulto
    40-59: Adulto
    60-...: Adulto mayor
5.Guardar el resultado como csv
Encapsula toda la lógica anterior en una función que reciba un dataframe como entrada.
"""""
import pandas as pd
import os
import numpy as np

if not os.path.exists("heart_failure_clinical_records_dataset.csv"):
    raise FileNotFoundError("El archivo no se encuentra descargado, ejecute la parte 4")

df = pd.read_csv("heart_failure_clinical_records_dataset.csv")

if df.isnull().sum().sum() > 0: # Verificar valores faltantes
    raise ValueError("El dataframe contiene valores faltantes")

df = df.drop_duplicates() # Verificar datos dupicados y eliminarlos

for col in df.columns:
    q1 = df[col].describe()["25%"]
    q3 = df[col].describe()["75%"]
    iqr = q3 - q1

    # Identificamos los valores atípicos
    outliers = df[col].loc[(df[col] < q1 - 1.5 * iqr) | (df[col] > q3 + 1.5 * iqr)]

    # Eliminamos los valores atípicos
    df = df.drop(outliers.index)

# Columna con de categoria edades
df["edad_categoria"] = pd.cut(df["age"], [0, 12, 19, 39, 59, np.inf],
labels=["Niño", "Adolescente", "Jóvenes adulto", "Adulto", "Adulto mayor"])

df.to_csv("heart_failure_clinical_records_dataset_limpio.csv", index=False)