import math
from cargar_datos import cargar_datos


def tres_cifras_significativas(x):
    return round(x, -(int(math.floor(math.log10(abs(x)))) - 2))

def dos_cifras_significativas(x):
    return round(x, -(int(math.floor(math.log10(abs(x)))) - 1))

def error_absoluto(real, aprox):
    return abs(real - aprox)


def error_relativo(real, aprox):
    ea = error_absoluto(real, aprox)
    return (ea / real) * 100

def propagacion_mult_div(err1,err2):
    return err1 + err2

def propagacion_sum_res(err1,err2):
    return err1 + err2


if __name__ == "__main__":
    print("\n--- A1 ---")
    datos = cargar_datos()

    precios = datos[:,3]

    aproximados = []
    for precio in precios:
        aproximados.append(dos_cifras_significativas(precio))


    errores_abs = []
    for real, aprox in zip(precios, aproximados):
        errores_abs.append(error_absoluto(real, aprox))

    errores_rel = []
    for real, aprox in zip(precios, aproximados):
        errores_rel.append(error_relativo(real, aprox))

    for i in range(48):
        print(
            f"Real: {precios[i]} | "
            f"Aprox: {aproximados[i]} | "
            f"Ea: {errores_abs[i]:.2f} | "
            f"Er: {errores_rel[i]:.4f}%"
        )



    mayor_error = max(errores_rel)
    indice = errores_rel.index(mayor_error)

    print("\nMayor error relativo:")
    print(f"Indice: {indice}")
    print(f"Precio real: {precios[indice]:.2f}")
    print(f"Precio aproximado: {aproximados[indice]:.2f}")
    print(f"Error relativo: {mayor_error:.4f}%")

    print("\n--- A2 ---")
    #elijo una compra y una venta
    precio_compra = 799.19    # Marzo 2022
    precio_venta = 1000.76    # Enero 2025

    monto = 1000000

    aprox_compra = dos_cifras_significativas(precio_compra)
    aprox_venta = dos_cifras_significativas(precio_venta)

    err_compra = error_relativo(precio_compra, aprox_compra)
    err_venta = error_relativo(precio_venta, aprox_venta)

    usd = monto / aprox_compra
    pesos_final = usd * aprox_venta
    ganancia = pesos_final - monto

    error_rel_total = propagacion_mult_div(err_compra, err_venta)
    error_abs_ganancia = (ganancia * error_rel_total) / 100

    print(f"Precio compra: {precio_compra}")
    print(f"Precio venta: {precio_venta}")
    print(f"USD comprados: {usd:.2f}")
    print(f"Pesos finales: {pesos_final:.2f}")
    print(f"Ganancia: {ganancia:.2f} ± {error_abs_ganancia:.2f}")
    print(f"Error porcentual: {error_rel_total:.4f}%")


    print("\n--- A3 ---")
    p1 = 875.66
    p2 = 874.67

    p1_aprox = tres_cifras_significativas(p1)
    p2_aprox = tres_cifras_significativas(p2)

    delta_p = p2_aprox - p1_aprox
    e1 = error_absoluto(p1, p1_aprox)
    e2 = error_absoluto(p2,p2_aprox)

    error_delta = propagacion_sum_res(e1, e2)

    error_porcentual = (error_delta / abs(delta_p)) * 100


    print(f"ΔP = {delta_p:.2f} ± {error_delta:.2f}")
    print(f"Error porcentual = {error_porcentual:.2f}%")


    print("\n--- A5 ---")
    precio_min = min(precios)
    precio_max = max(precios)

    indice_min = precios.tolist().index(precio_min)
    indice_max = precios.tolist().index(precio_max)


    print(f"Precio minimo: {precio_min}")
    print(f"Precio maximo: {precio_max}")
    print(f"Indice minimo: {indice_min}")
    print(f"Indice maximo: {indice_max}")

    anios = datos[:,0]
    meses = datos[:,2]

    print(f"Año minimo: {int(anios[indice_min])}")
    print(f"Mes minimo: {int(meses[indice_min])}")

    print(f"Año maximo: {int(anios[indice_max])}")
    print(f"Mes maximo: {int(meses[indice_max])}")

    #recalculamos la rentabilidad

    monto = 1000000

    aprox_compra = dos_cifras_significativas(precio_min)
    aprox_venta = dos_cifras_significativas(precio_max)

    usd = monto / aprox_compra

    pesos_final = usd * aprox_venta

    ganancia = pesos_final - monto

    rentabilidad = (ganancia / monto) * 100

    er_compra = error_relativo(precio_min, aprox_compra)

    er_venta = error_relativo(precio_max, aprox_venta)

    error_rel_total = propagacion_mult_div(er_compra, er_venta)

    error_abs_ganancia = (ganancia * error_rel_total) / 100


    print(f"Rentabilidad = {rentabilidad:.2f}%")
    print(f"Ganancia = {ganancia:.2f} ± {error_abs_ganancia:.2f}")
    print(f"Error porcentual = {error_rel_total:.4f}%")
