import matplotlib.pyplot as plt

from funciones import f1, g1, df1, ddf1

from biseccion import biseccion
from falsa_posicion import falsa_posicion
from punto_fijo import punto_fijo
from secante import secante
from newton_raphson import newton_raphson
from newton_raphson_mejorado import newton_raphson_mejorado


plt.figure(figsize=(10, 6))


# Bisección
raiz, datos = biseccion(f1, 1, 2, 1e-6, 100)
errores = [fila[-1] for fila in datos]
plt.plot(range(1, len(errores) + 1), errores, marker="o", label="Bisección")


# Falsa Posición
raiz, datos = falsa_posicion(f1, 1, 2, 1e-6, 100)
errores = [fila[-1] for fila in datos]
plt.plot(range(1, len(errores) + 1), errores, marker="o", label="Falsa Posición")


# Punto Fijo
raiz, datos = punto_fijo(g1, 1.5, 1e-6, 100)
errores = [fila[-1] for fila in datos]
plt.plot(range(1, len(errores) + 1), errores, marker="o", label="Punto Fijo")


# Secante
raiz, datos = secante(f1, 1, 2, 1e-6, 100)
errores = [fila[-1] for fila in datos]
plt.plot(range(1, len(errores) + 1), errores, marker="o", label="Secante")


# Newton-Raphson
raiz, datos = newton_raphson(f1, df1, 1.5, 1e-6, 100)
errores = [fila[-1] for fila in datos]
plt.plot(range(1, len(errores) + 1), errores, marker="o", label="Newton-Raphson")


# Newton-Raphson Mejorado
raiz, datos = newton_raphson_mejorado(
    f1,
    df1,
    ddf1,
    1.5,
    1e-6,
    100
)
errores = [fila[-1] for fila in datos]
plt.plot(
    range(1, len(errores) + 1),
    errores,
    marker="o",
    label="Newton-Raphson Mejorado"
)


plt.title("Comparación de Convergencia de Métodos")
plt.xlabel("Iteración")
plt.ylabel("Error")
plt.grid(True)
plt.legend()

plt.savefig("../assets/comparacion_convergencia.png")
plt.close()

print("Gráfico guardado correctamente.")