"""Tu tarea en esta etapa del proyecto consiste en crear un script (un archivo .py) que realice todas las operaciones vistas hasta ahora (desde el módulo de APIS) que al ejecutarse

Descargue los datos desde una url
Convierta todo a un dataframe
Categorice en grupos
Exporte un csv resultante"""""

import requests
import pandas as pd
import os
import sys
import numpy as np

def data_download(url):
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        print(response.text)
        filename = url.split('/')[-1]
        with open(filename, "wb") as file:
            file.write(response.content)
        df = pd.read_csv(filename)
        return df
    else:
        print("Error:", response.status_code, response.text)
        return None

def clean_data(df):
    missing = df.isnull().sum().sum() #valores faltantes
    if missing > 0:
        print(f"Tiene {missing} valores faltantes.")
    else:
        print("No tiene valores faltantes")
    
    duplicates = df.duplicated().sum() #valores duplicados
    if duplicates > 0:
        print(f"Tiene {duplicates} valores duplicados.")
    else:
        print("No tiene valores duplicados")
    return df     

def group_categorie(df):
    df["edad_categoria"] = pd.cut(df["age"], [0, 12, 19, 39, 59, np.inf],
    labels=["Niño", "Adolescente", "Jóvenes adulto", "Adulto", "Adulto mayor"])
    return df

def csv_export(df, file):
    df.to_csv(file, index=False)
    print(f"Datos exportados a (file)")

def main():
    if len(sys.argv) != 2:
        print("Ingrese la URL:")
        sys.exit(1)
    else:
        url = sys.argv[1]
        df = data_download(url)

        if df is not None:
            print(df.head())
        else:
            print("Error al descargar el archivo")
    
    try:
        print("20%")
        df = pd.DataFrame(df) 
        print("40%")
        df = clean_data(df)
        print("60%")
        df = group_categorie(df)
        print("80%")
        file = "datos_procesados.csv"
        csv_export(df, file)
        print("100%")
    except Exception as e:
        print(f"Error: (e)")

if __name__ == "__main__":
    main()