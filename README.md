# Problema 2: Dólar Observado SII (2022-2025)

## Integrante

* Andy Rivera Olguín

## Descripción

Este proyecto corresponde al Laboratorio 1 de Computación Numérica de la Universidad Católica del Maule.

El objetivo fue analizar errores numéricos utilizando los datos del dólar observado del Servicio de Impuestos Internos (SII) entre enero de 2022 y diciembre de 2025\. Se estudiaron conceptos como cifras significativas, error absoluto, error relativo, propagación de errores, cancelación numérica y representación en punto flotante.

Además, se realizó un análisis de compra y venta de dólares para determinar cuándo conviene comprar y vender considerando la incertidumbre asociada a los cálculos.

## Estructura del proyecto

problema2-dolar-sii/  
├── README.md  
├── INFORME.pdf  
├── requirements.txt  
│  
├── data/  
│   └── dolar\_observado\_sii\_2022\_2025.csv  
│  
├── src/  
│   ├── cargar\_datos.py  
│   ├── errores.py  
│   ├── anualidad.py  
│   ├── punto\_flotante.py  
│   └── graficos.py  
│  
└── graficos/  
    ├── serie\_dolar.png  
    ├── variacion\_mensual.png  
    ├── error\_representacion.png  
    ├── rentabilidad.png  
    └── deriva\_punto\_flotante.png

## Descripción de los programas

### cargar\_datos.py

Carga el archivo CSV utilizando NumPy y entrega los datos para ser utilizados en los demás módulos.

### errores.py

Calcula:

* Error absoluto.  
* Error relativo.  
* Propagación de errores.  
* Error de representación (A1).  
* Compra y venta de dólares (A2).  
* Cancelación numérica (A3).  
* Mejor compra y mejor venta (A5).

### anualidad.py

Calcula la variación entre enero y diciembre de cada año junto con su error propagado (A4).

### punto\_flotante.py

Analiza el comportamiento de números en punto flotante:

* Mantisa corta y cifras significativas.  
* Deriva producida por conversiones repetidas.  
* Comparación entre float32 y float64.  
* Cancelación numérica.

### graficos.py

Genera los cinco gráficos requeridos por el laboratorio mediante Matplotlib.

## Requisitos

Instalar las dependencias:

pip install \-r requirements.txt

## Ejecución

Desde la carpeta `src` ejecutar:

python errores.py  
python anualidad.py  
python punto\_flotante.py  
python graficos.py

## Resultados principales

* El mayor error relativo de representación se produjo en abril de 2022 con un error de 0.5987%.  
* La mejor compra se encontró en febrero de 2023 con un valor de 798.26 CLP/USD.  
* La mejor venta se encontró en enero de 2025 con un valor de 1000.76 CLP/USD.  
* La mejor estrategia produjo una rentabilidad aproximada de 25.00%.  
* El fenómeno de cancelación numérica quedó evidenciado al comparar diciembre de 2022 y diciembre de 2023, obteniendo un error porcentual de 67.00%.  
* La deriva observada utilizando float32 se mantuvo entre \-0.0625 y 0.0625 CLP.


## Archivos generados

* resultados\_anualidad.csv: contiene las variaciones anuales junto con el error propagado y el error porcentual calculado para cada año.

## Conclusión

Los resultados muestran que pequeñas diferencias entre valores cercanos pueden quedar dominadas por el error numérico. Por esta razón, al analizar datos financieros o científicos no basta con observar el resultado obtenido; también es necesario considerar la incertidumbre asociada a cada cálculo. 