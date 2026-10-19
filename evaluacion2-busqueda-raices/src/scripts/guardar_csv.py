import pandas as pd

def guardar_csv(datos, columnas, nombre_archivo):

    df = pd.DataFrame(datos, columns=columnas)

    df.to_csv(nombre_archivo, index=False)

    print(f"Archivo {nombre_archivo} guardado correctamente.")