import numpy as np
import matplotlib.pyplot as plt

def graficar_funcion(f, raiz, inicio, fin, nombre_archivo):

    x = np.linspace(inicio, fin, 500)
    y = f(x)

    plt.figure(figsize=(8, 5))

    plt.plot(x, y, label="f(x)")
    plt.axhline(0, color="black")

    plt.scatter(
        raiz,
        f(raiz),
        color="red",
        s=100,
        label=f"Raíz ≈ {raiz:.6f}"
    )

    plt.title("Función y raíz encontrada")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()

    plt.savefig(nombre_archivo)
    plt.close()