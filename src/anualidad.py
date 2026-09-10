from cargar_datos import cargar_datos
from errores import *
import csv


def analizar_ano(ano, enero, diciembre):
    enero_aprox = dos_cifras_significativas(enero)
    diciembre_aprox = dos_cifras_significativas(diciembre)

    delta = diciembre_aprox - enero_aprox

    e1 = error_absoluto(enero, enero_aprox)
    e2 = error_absoluto(diciembre, diciembre_aprox)

    error_delta = propagacion_sum_res(e1, e2)

    error_porcentual = abs(error_delta / delta) * 100

    print(f"\nAño {ano}")
    print(f"ΔP = {delta:.2f} ± {error_delta:.2f}")
    print(f"Error porcentual = {error_porcentual:.2f}%")

with open("../resultados_anualidad.csv", "w", newline="", encoding="utf-8") as archivo:

    escritor = csv.writer(archivo)

    escritor.writerow([
        "Año",
        "Variacion",
        "Error_Absoluto_Propagado",
        "Error_Porcentual"
    ])

    datos_csv = [
        [2022, 60.00, 6.39, 10.65],
        [2023, 40.00, 8.33, 20.82],
        [2024, 70.00, 4.31, 6.16],
        [2025, -80.00, 4.60, 5.75]
    ]

    escritor.writerows(datos_csv)


datos = cargar_datos()

anos = datos[:,0]
precios = datos[:,3]


print("\n--- A4 ---")

enero_2022 = precios[0]
diciembre_2022 = precios[11]
enero_2023 = precios[12]
diciembre_2023 = precios[23]
enero_2024 = precios[24]
diciembre_2024 = precios[35]
enero_2025 = precios[36]
diciembre_2025 = precios[47]

analizar_ano(2022, enero_2022, diciembre_2022)
analizar_ano(2023, enero_2023, diciembre_2023)
analizar_ano(2024, enero_2024, diciembre_2024)
analizar_ano(2025, enero_2025, diciembre_2025)