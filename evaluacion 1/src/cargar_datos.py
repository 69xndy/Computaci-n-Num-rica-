import numpy as np


def cargar_datos():
    datos = np.genfromtxt("../data/dolar_observado_sii_2022_2025.csv", delimiter=",",skip_header=1)
    return datos

