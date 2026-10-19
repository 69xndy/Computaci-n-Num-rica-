import matplotlib.pyplot as plt

def graficar_convergencia(datos):

    iteraciones = []
    errores = []

    for fila in datos:
        iteraciones.append(fila[0])
        errores.append(fila[-1])

    plt.plot(iteraciones, errores, marker="o")

    plt.title("Convergencia del Método")
    plt.xlabel("Iteración")
    plt.ylabel("Error")

    plt.grid(True)

    plt.show()