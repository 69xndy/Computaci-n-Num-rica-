def newton_raphson_mejorado(f, df, ddf, p0, tolerancia, max_iter):

    iteraciones = []

    for i in range(max_iter):

        p = p0 - (f(p0) * df(p0)) / ((df(p0)**2) - f(p0) * ddf(p0))

        error = abs(p - p0)

        iteraciones.append([i + 1, p0, p, error])

        if error < tolerancia:
            return p, iteraciones

        p0 = p

    return p, iteraciones