import pandas as pd

from funciones import f1, g1, df1, ddf1

from biseccion import biseccion
from falsa_posicion import falsa_posicion
from punto_fijo import punto_fijo
from secante import secante
from newton_raphson import newton_raphson
from newton_raphson_mejorado import newton_raphson_mejorado

datos_resumen = []

raiz, datos = biseccion(f1, 1, 2, 1e-6, 100)
datos_resumen.append(["Biseccion", raiz, len(datos)])

raiz, datos = falsa_posicion(f1, 1, 2, 1e-6, 100)
datos_resumen.append(["Falsa Posicion", raiz, len(datos)])

raiz, datos = punto_fijo(g1, 1.5, 1e-6, 100)
datos_resumen.append(["Punto Fijo", raiz, len(datos)])

raiz, datos = secante(f1, 1, 2, 1e-6, 100)
datos_resumen.append(["Secante", raiz, len(datos)])

raiz, datos = newton_raphson(f1, df1, 1.5, 1e-6, 100)
datos_resumen.append(["Newton-Raphson", raiz, len(datos)])

raiz, datos = newton_raphson_mejorado(
    f1,
    df1,
    ddf1,
    1.5,
    1e-6,
    100
)
datos_resumen.append(["Newton-Raphson Mejorado", raiz, len(datos)])

df = pd.DataFrame(
    datos_resumen,
    columns=["Metodo", "Raiz", "Iteraciones"]
)

df.to_csv("../data/resumen_convergencia.csv", index=False)

print(df)