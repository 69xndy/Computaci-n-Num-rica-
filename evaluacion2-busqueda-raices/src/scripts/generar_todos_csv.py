from funciones import f1, f2, f3, f4, f5, f6
from generar_datos_funcion import generar_datos_funcion

generar_datos_funcion(f1, 1, 2, 100, "../data/f1_datos.csv")
generar_datos_funcion(f2, 1, 3, 100, "../data/f2_datos.csv")
generar_datos_funcion(f3, 2, 3, 100, "../data/f3_datos.csv")
generar_datos_funcion(f4, 0, 1, 100, "../data/f4_datos.csv")
generar_datos_funcion(f5, 0, 1, 100, "../data/f5_datos.csv")
generar_datos_funcion(f6, 0.1, 1, 100, "../data/f6_datos.csv")