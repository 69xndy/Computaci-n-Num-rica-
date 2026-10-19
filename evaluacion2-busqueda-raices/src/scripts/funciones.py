import numpy as np

# Polinómica (raíz simple)
def f1(x):
    return x**3 - x - 2

# Polinómica (raíz doble)
def f2(x):
    return (x - 2)**2

# Logarítmica
def f3(x):
    return np.log(x) + x - 4

# Exponencial
def f4(x):
    return np.exp(-x) - x

# Trigonométrica
def f5(x):
    return np.cos(x) - x

# Mixta
def f6(x):
    return np.sqrt(x) - np.cos(x)

#para usar en punto fijo
def g1(x):
    return (x + 2)**(1/3)

#derivada para newton
def df1(x):
    return 3*x**2 - 1

#segunda derivada
def ddf1(x):
    return 6*x
