"""Continuando con la anterior sección del proyecto integrador, ahora debes realizar lo siguiente:

Convertir la estructura Dataset en un DataFrame de Pandas usando pd.DataFrame.
Separar el dataframe en dos diferentes, uno conteniendo las filas con personas que perecieron (is_dead=1) y otro con el complemento.
Calcular los promedios de las edades de cada dataset e imprimir."""""

import pandas as pd

def convertidor_a_dataframe(ruta_archivo: str) -> pd.DataFrame:
    df = pd.read_csv(ruta_archivo)
    return df

ruta_completa = "C:/Python/NumPy/Proyecto_analisis_datos/heart_failure_clinical_records_dataset.csv"
dataframe_resultante = convertidor_a_dataframe(ruta_completa)
print(dataframe_resultante.head())

def perecieron(df: pd.DataFrame) -> tuple:
    fallecidos = df.loc[df['DEATH_EVENT'] == 1]
    no_fallecidos = df.loc[df['DEATH_EVENT'] == 0]
    print("Personas fallecidas:")
    print(fallecidos)
    
    print("\nPersonas no fallecidas:")
    print(no_fallecidos)
    
    return fallecidos, no_fallecidos

fallecidos, no_fallecidos = perecieron(dataframe_resultante)

def calcular_promedio_edades(df: pd.DataFrame) -> float:
    promedio_edades = df['age'].mean()
    return promedio_edades

promedio_edades_total = calcular_promedio_edades(dataframe_resultante)
print(f"Promedio de edades en el dataset completo: {promedio_edades_total}")

promedio_edades_fallecidos = calcular_promedio_edades(fallecidos)
print(f"Promedio de edades en el dataset de personas fallecidas: {promedio_edades_fallecidos}")

promedio_edades_no_fallecidos = calcular_promedio_edades(no_fallecidos)
print(f"Promedio de edades en el dataset de personas no fallecidas: {promedio_edades_no_fallecidos}")

