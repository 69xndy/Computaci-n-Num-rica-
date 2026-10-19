import matplotlib.pyplot as plt
import numpy as np
from cargar_datos import cargar_datos
from errores import (dos_cifras_significativas,error_relativo)

def grafico_serie_dolar(precios):

    meses = np.arange(1, len(precios)+1)

    plt.figure(figsize=(12,6))

    plt.plot(
        meses,
        precios,
        marker="o"
    )

    plt.title("Dolar observado 2022-2025")
    plt.xlabel("Mes")
    plt.ylabel("CLP/USD")

    plt.grid(True)

    plt.tight_layout()

    plt.savefig("../graficos/serie_dolar.png")

    plt.close()


def grafico_variacion(precios):

    delta_p = np.diff(precios)

    plt.figure(figsize=(12,6))

    plt.bar(
        range(len(delta_p)),
        delta_p
    )

    plt.title("Variacion mensual del dolar")
    plt.xlabel("Mes")
    plt.ylabel("ΔP")

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        "../graficos/variacion_mensual.png"
    )

    plt.close()

def grafico_error_representacion(precios):

    aproximados = []

    for precio in precios:
        aproximados.append(
            dos_cifras_significativas(precio)
        )

    errores_rel = []

    for real, aprox in zip(precios, aproximados):
        errores_rel.append(
            error_relativo(real, aprox)
        )

    plt.figure(figsize=(12,6))

    plt.bar(
        range(len(errores_rel)),
        errores_rel
    )

    plt.title(
        "Error relativo de representacion"
    )

    plt.xlabel("Mes")
    plt.ylabel("Error relativo (%)")

    plt.grid(True, axis="y")

    plt.tight_layout()

    plt.savefig(
        "../graficos/error_representacion.png"
    )

    plt.close()

def grafico_rentabilidad(precios):

    indice_min = 13

    precio_compra = precios[indice_min]

    rentabilidades = []

    for precio_venta in precios[indice_min + 1:]:

        rentabilidad = (
            (precio_venta - precio_compra)
            / precio_compra
        ) * 100

        rentabilidades.append(rentabilidad)

    plt.figure(figsize=(12,6))

    plt.plot(
        rentabilidades,
        marker="o"
    )

    plt.title(
        "Rentabilidad comprando en el minimo"
    )

    plt.xlabel("Mes posterior")
    plt.ylabel("Rentabilidad (%)")

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        "../graficos/rentabilidad.png"
    )

    plt.close()

def grafico_deriva(precios):

    monto = np.float32(1000000)

    derivas = []

    for precio in precios:

        precio = np.float32(precio)

        usd = monto / precio

        pesos_final = usd * precio

        deriva = pesos_final - monto

        derivas.append(deriva)

    plt.figure(figsize=(12,6))

    plt.plot(
        derivas,
        marker="o"
    )

    plt.axhline(
        0,
        color="black",
        linewidth=1
    )

    plt.title(
        "Deriva de la ida y vuelta en punto flotante"
    )

    plt.xlabel("Mes")
    plt.ylabel("Deriva (CLP)")

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        "../graficos/deriva_punto_flotante.png"
    )

    plt.close()


if __name__ == "__main__":

    datos = cargar_datos()

    precios = datos[:,3]

    grafico_serie_dolar(precios)

    grafico_variacion(precios)

    grafico_error_representacion(precios)

    grafico_rentabilidad(precios)

    grafico_deriva(precios)

    print("Graficos generados correctamente")