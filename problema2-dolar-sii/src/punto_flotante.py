import math
import numpy as np
from cargar_datos import cargar_datos

def tres_cifras_significativas(x):
    return round(x, -(int(math.floor(math.log10(abs(x)))) - 2))



if __name__ == "__main__":

    precio = 1000.76

    aprox = tres_cifras_significativas(precio)

    error = abs(precio - aprox)

    print("--- B1 ---")
    print(f"Valor real = {precio}")
    print(f"Valor aproximado = {aprox}")
    print(f"Error de representacion = {error:.2f}")

    print("\n--- B2 ---")

    datos = cargar_datos()
    precios = datos[:,3]
    derivas = []
    monto = np.float32(1000000)

    for precio in precios:

        precio = np.float32(precio)

        usd = monto / precio

        pesos_final = usd * precio

        deriva = pesos_final - monto

        derivas.append(deriva)

    print(f"Mayor deriva = {max(derivas)}")
    print(f"Menor deriva = {min(derivas)}")


    print("\n--- B4 ---")

    a32 = np.float32(874.67)
    b32 = np.float32(875.66)
    resultado32 = a32 - b32
    print("float32 =", resultado32)

    a64 = np.float64(874.67)
    b64 = np.float64(875.66)
    resultado64 = a64 - b64
    print("float64 =", resultado64)

    valor_real = 874.67 - 875.66
    print("valor real =", valor_real)