from datasets import load_dataset
import numpy as np

dataset = load_dataset("mstz/heart_failure")

data = dataset["train"]

edades = np.array(data["age"])
promedio_edad = np.mean(edades)

print("Promedio de edad:", promedio_edad)