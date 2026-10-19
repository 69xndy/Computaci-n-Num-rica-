# Evaluación 2: La raíz que se esconde

## Descripción

Este proyecto implementa y analiza distintos métodos numéricos para la búsqueda de raíces de ecuaciones no lineales utilizando Python.

Se desarrollaron los siguientes métodos:

- Bisección
- Falsa Posición
- Punto Fijo
- Secante
- Newton-Raphson
- Newton-Raphson Mejorado

Además, se generaron gráficos de las funciones estudiadas, gráficos de convergencia y archivos CSV con los datos obtenidos.

---

## Objetivos

- Implementar métodos clásicos de búsqueda de raíces.
- Comparar el comportamiento de cada método.
- Analizar la velocidad de convergencia.
- Estudiar el efecto de diferentes funciones e intervalos.
- Generar evidencia mediante gráficos y archivos CSV.

---

## Funciones Analizadas

### Función 1 (Polinómica)

f(x) = x³ - x - 2

Intervalo: [1, 2]

### Función 2 (Raíz doble)

f(x) = (x - 2)²

Estimación inicial: x₀ = 1.2

### Función 3 (Logarítmica)

f(x) = ln(x) + x - 4

Intervalo: [2, 3]

### Función 4 (Exponencial)

f(x) = e⁻ˣ - x

Intervalo: [0, 1]

### Función 5 (Trigonométrica)

f(x) = cos(x) - x

Intervalo: [0, 1]

### Función 6 (Mixta)

f(x) = √x - cos(x)

Intervalo: [0.1, 1]

---

## Tolerancia Utilizada

Todas las pruebas fueron realizadas utilizando una tolerancia de:

```python
1e-6
```

Este valor fue utilizado como criterio de detención para todos los métodos implementados.

---

## Dependencias

Para ejecutar el proyecto se requieren las siguientes bibliotecas:

```text
numpy
matplotlib
pandas
```

Instalación:

```bash
pip install -r requirements.txt
```

---

## Estructura del Proyecto

```text
evaluacion2-busqueda-raices
│
├── README.md
├── requirements.txt
├── informe.md
│
└── src
    ├── assets
    │   ├── f1.png
    │   ├── f2.png
    │   ├── f3.png
    │   ├── f4.png
    │   ├── f5.png
    │   ├── f6.png
    │   └── comparacion_convergencia.png
    │
    ├── data
    │   ├── f1_datos.csv
    │   ├── f2_datos.csv
    │   ├── f3_datos.csv
    │   ├── f4_datos.csv
    │   ├── f5_datos.csv
    │   ├── f6_datos.csv
    │   └── resumen_convergencia.csv
    │
    └── scripts
        ├── funciones.py
        ├── biseccion.py
        ├── falsa_posicion.py
        ├── punto_fijo.py
        ├── secante.py
        ├── newton_raphson.py
        ├── newton_raphson_mejorado.py
        ├── guardar_csv.py
        ├── generar_datos_funcion.py
        ├── generar_todos_csv.py
        ├── generar_todos_graficos.py
        ├── graficar_funcion.py
        ├── grafico_convergencia.py
        └── resumen_convergencia.py
```

---

## Resultados Obtenidos para f(x)=x³−x−2

| Método | Iteraciones |
|----------|----------|
| Bisección | 20 |
| Falsa Posición | 13 |
| Punto Fijo | 7 |
| Secante | 7 |
| Newton-Raphson | 3 |
| Newton-Raphson Mejorado | 3 |

Raíz aproximada encontrada:

```text
x ≈ 1.52138
```

---

## Análisis General

Los resultados mostraron que todos los métodos implementados fueron capaces de aproximar correctamente la raíz de la función analizada.

Los métodos de Newton-Raphson y Newton-Raphson Mejorado alcanzaron la solución utilizando la menor cantidad de iteraciones, mientras que el método de Bisección requirió más pasos para cumplir la tolerancia establecida.

La Secante obtuvo un desempeño intermedio, logrando una convergencia rápida sin necesidad de calcular derivadas. Por otro lado, la función con raíz doble permitió comprobar que no siempre existe cambio de signo cuando una función posee una raíz, lo que limita la aplicación de algunos métodos cerrados.

Los gráficos y archivos CSV generados permitieron visualizar y comparar el comportamiento de todos los algoritmos estudiados.

---

## Archivos Generados

### Gráficos

- f1.png
- f2.png
- f3.png
- f4.png
- f5.png
- f6.png
- comparacion_convergencia.png

### Archivos CSV

- f1_datos.csv
- f2_datos.csv
- f3_datos.csv
- f4_datos.csv
- f5_datos.csv
- f6_datos.csv
- resumen_convergencia.csv

---

## Autor

Andy G. Rivera Olguín

Computación Numérica

Universidad Católica del Maule