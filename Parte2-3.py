"""Continuando con la anterior sección del proyecto integrador, ahora debes realizar lo siguiente:

Convertir la estructura Dataset en un DataFrame de Pandas usando pd.DataFrame.
Separar el dataframe en dos diferentes, uno conteniendo las filas con personas que perecieron (is_dead=1) y otro con el complemento.
Calcular los promedios de las edades de cada dataset e imprimir.
Verificar que los tipos de datos son correctos en cada colúmna (por ejemplo que no existan colúmnas numéricas en formato de cadena).
Calcular la cantidad de hombres fumadores vs mujeres fumadoras (usando agregaciones en Pandas).
"""""

import pandas as pd

def convertir_a_dataframe(ruta_archivo: str) -> pd.DataFrame:
    df = pd.read_csv(ruta_archivo)
    return df

def corregir_tipo_edad(df: pd.DataFrame) -> pd.DataFrame:
    df['age'] = df['age'].astype(int)
    return df

def verificar_tipos_de_datos(df: pd.DataFrame) -> None:
    tipos_de_datos = df.dtypes
    print("Tipos de datos en cada columna:")
    print(tipos_de_datos)

def analizar_fallecidos(df: pd.DataFrame) -> tuple:
    fallecidos = df.loc[df['DEATH_EVENT'] == 1]
    no_fallecidos = df.loc[df['DEATH_EVENT'] == 0]
    print("Personas fallecidas:")
    print(fallecidos)
    
    print("\nPersonas no fallecidas:")
    print(no_fallecidos)
    
    return fallecidos, no_fallecidos

def calcular_promedio_edades(df: pd.DataFrame) -> float:
    promedio_edades = df['age'].mean()
    return promedio_edades

def calcular_cantidad_fumadores(df: pd.DataFrame) -> pd.DataFrame:
    resultados = df.groupby(['sex', 'smoking']).size().unstack().fillna(0)
    return resultados

# Cargar el DataFrame
ruta_completa = "C:/Python/NumPy/Proyecto_analisis_datos/heart_failure_clinical_records_dataset.csv"
dataframe_resultante = convertir_a_dataframe(ruta_completa)

# Corregir tipo de datos
dataframe_resultante = corregir_tipo_edad(dataframe_resultante)

# Verificar tipos de datos
verificar_tipos_de_datos(dataframe_resultante)

# Analizar fallecidos
fallecidos, no_fallecidos = analizar_fallecidos(dataframe_resultante)

# Calcular promedios de edades
promedio_edades_total = calcular_promedio_edades(dataframe_resultante)
print(f"Promedio de edades en el dataset completo: {promedio_edades_total}")

promedio_edades_fallecidos = calcular_promedio_edades(fallecidos)
print(f"Promedio de edades en el dataset de personas fallecidas: {promedio_edades_fallecidos}")

promedio_edades_no_fallecidos = calcular_promedio_edades(no_fallecidos)
print(f"Promedio de edades en el dataset de personas no fallecidas: {promedio_edades_no_fallecidos}")

# Calcular cantidad de fumadores
resultados_ejemplo = calcular_cantidad_fumadores(dataframe_resultante)
print("Cantidad de hombres fumadores y mujeres fumadoras:")
print(resultados_ejemplo)