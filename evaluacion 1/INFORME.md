## **Laboratorio 1: Análisis de Error con el Dólar Observado del SII (2022-2025)**

### Integrante: Andy Rivera Olguin

---

# **Introducción**

El objetivo de este trabajo fue analizar los errores numéricos producidos por la representación aproximada de números utilizando pocas cifras significativas, de forma similar a como los computadores almacenan números en punto flotante. Para ello se utilizó el conjunto de datos del dólar observado del Servicio de Impuestos Internos (SII) entre enero de 2022 y diciembre de 2025\.

Se estudiaron errores absolutos, errores relativos, propagación de errores, cancelación numérica y efectos del punto flotante mediante simulaciones de compra y venta de dólares.

Los gráficos generados mediante Matplotlib se encuentran en la carpeta /graficos del repositorio.

---

# **A1. Error de representación mes a mes**

Cada valor del dólar fue aproximado utilizando dos cifras significativas.

El mayor error relativo encontrado fue:

* Año: 2022  
* Mes: Abril  
* Valor real: 815.12 CLP/USD  
* Valor aproximado: 820.00 CLP/USD  
* Error relativo: 0.5987%

Este resultado muestra que el redondeo produce diferentes niveles de error dependiendo del valor representado. Los errores observados fueron inferiores al 1%, aunque algunos meses resultaron más sensibles al redondeo que otros.

---

# **A2. Evaluación entre dos puntos (compra y venta)**

Se simuló una compra de dólares en marzo de 2022 utilizando un monto inicial de $1.000.000 CLP. El precio de compra fue 799.19 CLP/USD, que al aproximarse a dos cifras significativas se transformó en 800 CLP/USD. Para la venta se utilizó enero de 2025 con un valor de 1000.76 CLP/USD, aproximado a 1000 CLP/USD. La operación generó una ganancia aproximada de $250.000 CLP con una incertidumbre de ±$443.24. El error relativo propagado fue de 0.1773%, por lo que la ganancia es considerablemente mayor que la incertidumbre y la conclusión resulta confiable.

Se utilizó:

* Monto inicial: $1.000.000 CLP  
* Compra: Marzo 2022 (799.19 CLP/USD)  
* Venta: Enero 2025 (1000.76 CLP/USD)

Resultados:

* USD comprados: 1250.00 USD  
* Pesos finales: $1.250.000 CLP  
* Ganancia: $250.000 ± 443.24 CLP  
* Error porcentual: 0.1773%

---

# **A3. Cancelación (dos meses casi iguales)**

Se estudió la diferencia entre:

* Diciembre 2022: 875.66 CLP/USD  
* Diciembre 2023: 874.67 CLP/USD

Resultado:

* Variación (ΔP) \= \-1.00 ± 0.67  
* Error porcentual \= 67.00%

El error porcentual es extremadamente alto porque se están restando dos números muy parecidos. Este fenómeno se conoce como cancelación numérica.

Debido a que el error es comparable con la magnitud de la diferencia observada, no es posible afirmar con total confianza que exista una disminución significativa del valor del dólar entre ambos períodos.

---

# **A4. Anualidad (enero a diciembre)**

Se calculó la variación entre enero y diciembre para cada año.

### **Año 2022**

* Variación (ΔP) \= 60.00 ± 6.39  
* Error porcentual \= 10.65%

### **Año 2023**

* Variación (ΔP) \= 40.00 ± 8.33  
* Error porcentual \= 20.82%

### **Año 2024**

* Variación (ΔP) \= 70.00 ± 4.31  
* Error porcentual \= 6.16%

### **Año 2025**

* Variación (ΔP) \= \-80.00 ± 4.60  
* Error porcentual \= 5.75%

### **Orden de confiabilidad**

1. 2025 (5.75%)  
2. 2024 (6.16%)  
3. 2022 (10.65%)  
4. 2023 (20.82%)

Los años menos confiables presentan variaciones más pequeñas, por lo que el error propagado representa una fracción mayor del resultado.

---

# **A5. Mejor compra y mejor venta**

Precio mínimo encontrado:

* Febrero 2023  
* 798.26 CLP/USD

Precio máximo encontrado:

* Enero 2025  
* 1000.76 CLP/USD

Resultados:

* Rentabilidad \= 25.00%  
* Ganancia \= $250.000 ± 734.79 CLP  
* Error porcentual \= 0.2939%

La diferencia entre compra y venta es muy superior a la incertidumbre, por lo que la conclusión es sólida y robusta.

Además, la mejor estrategia encontrada durante todo el período fue comprar dólares en febrero de 2023 a un precio de 798.26 CLP/USD y venderlos en enero de 2025 a un precio de 1000.76 CLP/USD. Esta operación produjo una rentabilidad del 25.00% con un error propagado de 0.2939%, demostrando que la ganancia obtenida es significativamente mayor que la incertidumbre asociada al cálculo.

---

# **B1. Cifras significativas y mantisa corta**

Al almacenar un número con pocas cifras significativas, se conserva solamente una parte de su información y el resto se pierde por redondeo. Esto es similar a lo que ocurre en la representación de punto flotante de los computadores, donde la mantisa tiene una cantidad limitada de bits. Una mantisa más corta permite guardar menos información y produce un mayor error de representación.

Por ejemplo, el valor 1000.76 al aproximarse a tres cifras significativas se transforma en 1000\. El error absoluto de representación es:

∣1000.76−1000∣ \= 0.76

Por lo tanto:

Valor real \= 1000.76  
Valor aproximado \= 1000.00  
Error de representación \= 0.76

Este resultado muestra que al reducir la cantidad de cifras almacenadas se introduce una diferencia entre el valor real y el valor representado. De manera análoga, en un computador una mantisa con pocos bits genera errores de redondeo porque no puede almacenar todos los dígitos del número original.

---

# **B2. La ida y vuelta que no vuelve**

Se realizó una conversión:

Pesos → Dólares → Pesos

utilizando representación float32.

Resultados:

* Mayor deriva \= 0.0625 CLP  
* Menor deriva \= \-0.0625 CLP

La recuperación del monto inicial no siempre es exacta debido a los errores de redondeo propios de la representación en punto flotante. Estas diferencias son extremadamente pequeñas frente al monto inicial de $1.000.000 CLP, por lo que el efecto práctico es mínimo. Sin embargo, los resultados demuestran que las operaciones realizadas con números en punto flotante pueden introducir pequeñas desviaciones debido a la precisión finita con que los valores son almacenados por el computador.

---

# **B4. Cancelación en float32 y float64**

Se calculó:

874.67 − 875.66

Resultados:

* float32 \= \-0.98999023  
* float64 \= \-0.9900000000000091  
* valor real \= \-0.9900000000000091

Float64 conserva una mayor precisión que float32. Además, la operación evidencia el fenómeno de cancelación numérica, donde la resta de números muy cercanos provoca pérdida de cifras significativas.

---

# **Conclusión**

A partir de los datos analizados, el mejor momento para comprar dólares durante el período estudiado fue febrero de 2023, cuando el dólar observado alcanzó su valor mínimo de 798.26 CLP/USD. La diferencia respecto de los meses cercanos supera la incertidumbre asociada a la representación utilizada, por lo que este mínimo puede considerarse confiable. Por otro lado, el mejor momento para vender fue enero de 2025, cuando el dólar alcanzó su valor máximo de 1000.76 CLP/USD. Del mismo modo, la diferencia con los meses vecinos es suficientemente grande como para sostener esta conclusión con un alto nivel de confianza. 

La mejor estrategia encontrada consistió en comprar dólares en febrero de 2023 y venderlos en enero de 2025\. Esta operación produjo una rentabilidad aproximada de 25.00%, con una ganancia de $250.000 ± 734.79 CLP y un error propagado de 0.2939%. Debido a que la incertidumbre es muy pequeña en comparación con la ganancia obtenida, la recomendación puede considerarse sólida y robusta.

Sin embargo, no todos los tramos del análisis permiten realizar recomendaciones confiables. Un caso representativo corresponde a la comparación entre diciembre de 2022 y diciembre de 2023, donde la variación obtenida fue ΔP \= \-1.00 ± 0.67 y el error porcentual alcanzó 67.00%. En este escenario la incertidumbre es demasiado grande respecto del resultado observado, por lo que afirmar que el dólar realmente subió o bajó sería una conclusión poco confiable

**Lección aprendida:** Nunca se debe confiar en una diferencia pequeña sin analizar primero el error asociado.

