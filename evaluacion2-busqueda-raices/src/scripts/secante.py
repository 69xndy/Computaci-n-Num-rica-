def secante(f, p0, p1, tolerancia, max_iter):

    iteraciones = []

    for i in range(max_iter):

        p = p1 - f(p1) * (p1 - p0) / (f(p1) - f(p0))

        error = abs(p - p1)

        iteraciones.append([i + 1, p0, p1, p, error])

        if error < tolerancia:
            return p, iteraciones

        p0 = p1
        p1 = p

    return p, iteraciones