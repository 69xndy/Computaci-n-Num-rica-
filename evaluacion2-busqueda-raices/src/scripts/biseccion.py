def biseccion(f, a, b, tolerancia, max_iter):

    if f(a) * f(b) >= 0:
        print("No existe cambio de signo en el intervalo")
        return None

    iteraciones = []

    for i in range(max_iter):

        p = (a + b) / 2

        error = abs(b - a) / 2

        iteraciones.append([i + 1, a, b, p, f(p), error])

        if abs(f(p)) < tolerancia or error < tolerancia:
            return p, iteraciones

        if f(a) * f(p) < 0:
            b = p
        else:
            a = p

    return p, iteraciones