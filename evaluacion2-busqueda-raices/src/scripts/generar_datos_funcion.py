import numpy as np
import pandas as pd

def generar_datos_funcion(f, inicio, fin, cantidad, nombre_archivo):

    x = np.linspace(inicio, fin, cantidad)
    y = f(x)

    df = pd.DataFrame({
        "x": x,
        "f(x)": y
    })

    df.to_csv(nombre_archivo, index=False)

    print(f"Archivo {nombre_archivo} generado correctamente")