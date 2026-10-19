def falsa_posicion(f, a, b, tolerancia, max_iter):

    if f(a) * f(b) >= 0:
        print("No existe cambio de signo en el intervalo")
        return None

    iteraciones = []

    for i in range(max_iter):

        p = b - (f(b) * (b - a)) / (f(b) - f(a))

        error = abs(f(p))

        iteraciones.append([i + 1, a, b, p, f(p), error])

        if error < tolerancia:
            return p, iteraciones

        if f(a) * f(p) < 0:
            b = p
        else:
            a = p

    return p, iteraciones